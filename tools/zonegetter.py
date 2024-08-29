#!/usr/bin/env python3

import csv
import re
import requests
import sys

from npc.zones import zoneid_to_mapid


def fetch_zone_map():
    page = requests.get("https://wowhead.com")
    assert page, "Couldn't load wowhead"
    match = re.search(r'<script src="([^"]+data/global[^"]+)"', page.text)
    assert page, "Couldn't find globals script"
    page = requests.get(match.group(1))
    assert page, "Couldn't load wowhead zone map"
    match = re.search(r"WH\.setPageData\(.wow\.area\.names.,\s*({[^}]+})\);", page.text)
    assert match, "Locale JS didn't contain zone names"
    zone_map = {}
    for id, name in re.findall(r'"(\-?\d+)":"([^"]+)"', match.group(1)):
        zone_map[int(id)] = name
    return zone_map


def output_zone_map(zone_map, current_data):
    items = list(zone_map.items())
    items.sort()
    missing = []
    for zid, name in items:
        mapid = current_data.get(zid, False)
        if mapid:
            print("%d: %d,  # %s" % (zid, mapid, name))
        else:
            missing.append((zid, name))

    if missing:
        print("# Missing:")
        for data in missing:
            print("%d: False,  # %s" % data)


def update_zone_map_from_csv(current_data, filename):
    """Assumes the CSV file from Blizzard_Deprecated"""
    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        zonemap = {}
        for row in reader:
            if not row["DungeonMapID"] or row["DungeonFloor"] == "1":
                zonemap[int(row["WorldMapAreaID"])] = int(row["UiMapID"])

    new_data = {}
    for zoneid, mapid in current_data.items():
        new_data[zoneid] = zonemap.get(mapid)
        if mapid and not zonemap.get(mapid):
            print("FAILED", zoneid, mapid)
    return new_data


if __name__ == "__main__":
    if len(sys.argv) > 1:
        current_data = update_zone_map_from_csv(zoneid_to_mapid, sys.argv[1])
    else:
        current_data = zoneid_to_mapid

    output_zone_map(fetch_zone_map(), current_data)
