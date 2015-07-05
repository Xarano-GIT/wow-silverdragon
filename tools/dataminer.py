#!/usr/bin/env python3

import argparse
import sys

from npc import types as npctypes

blacklist = (
    50091, # untargetable Julak-Doom component
)
force_include = (
    17591, # Blood Elf Bandit
    50409, # Mysterious Camel Figurine
    50410, # Mysterious Camel Figurine (remnants)
    3868, # Blood Seeker (thought to share Aeonaxx's spawn timer)
    51236, # Aeonaxx (engaged)
    58336, # Darkmoon Rabbit
    # Lost and Found!
    64004, # Ghostly Pandaren Fisherman
    64191, # Ghostly Pandaren Craftsman
    65552, # Glinting Rapana Whelk
    64272, # Jade Warrior Statue
    64227, # Frozen Trail Packer
    #In 5.2, world bosses are no longer flagged as rare, even if they are.
    #Granted, 3 of 4 probably won't be rare. We include anyways because we always have.
    60491, # Sha of Anger
    62346, # Galleon
    69099, # Nalak
    69161, # Oondasta
    # On to Draenor
    71992, # Moonfang
    81001, # Nok-Karosh
    87308, # Gorok the Cleaver
    50990, # Nakk the Thunderer
    50981, # Luk'hok
    50985, # Poundfist
    51015, # Silthide
    50883, # Pathrunner
)
notes = {
    50410: "Crumbled Statue Remnants", # Mysterious Camel Figurine
    51401: "Red", # Madexx
    51402: "Green", # Madexx
    51403: "Black", # Madexx
    51404: "Blue", # Madexx
    50154: "Brown", # Madexx
    51236: "Engaged", # Aeonaxx
    69769: "Slate", # Zandalari Warbringer
    69841: "Amber", # Zandalari Warbringer
    69842: "Jade", # Zandalari Warbringer
}

def write_output(filename, data, strip = False):
    with open(filename, 'w') as f:
        f.write("""-- DO NOT EDIT THIS FILE; run dataminer.lua to regenerate.
local core = LibStub("AceAddon-3.0"):GetAddon("SilverDragon")
local module = core:GetModule("Data")
function module:GetDefaults()
\treturn {
""")
        for id, mob in sorted(data.items()):
            if id in blacklist:
                continue
            if id in notes:
                mob.add_notes(notes[id])
            if (not strip) or mob.data['locations']:
                f.write('\t\t[%d] = %s,\n' % (id, mob.to_lua()))
        f.write("""\t}
end
""")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Suck down a lot of data about rares")
    parser.add_argument('--wowhead', action='store_true', default=True)
    parser.add_argument('--no-wowhead', action='store_false', dest='wowhead')
    parser.add_argument('--wowdb', action='store_true', default=True)
    parser.add_argument('--no-wowdb', action='store_false', dest='wowdb')
    parser.add_argument('--strip-empties', action='store_true', dest='strip_empties')
    parser.add_argument('--ptr', action='store_true')
    ns = parser.parse_args()

    wowdb = {}
    wowhead = {}

    if ns.wowdb:
        print("LOADING FROM wowdb")
        from npc.wowdb import WowdbNPC
        for creature_type in npctypes.values():
            print("ACQUIRING rares for category", creature_type)
            wowdb.update(WowdbNPC.query(creature_type, ptr=ns.ptr))

        for id in force_include:
            if id not in wowdb:
                wowdb[id] = WowdbNPC(id, ptr=ns.ptr)

    if ns.wowhead:
        print("LOADING FROM wowhead")
        from npc.wowhead import WowheadNPC
        for categoryid, c in npctypes.items():
            print("ACQUIRING rares for category", categoryid, c)
            for expansion in range(1, 7):
                print("EXPANSION", expansion)
                # run per-expansion to avoid caps on results-displayed
                wowhead.update(WowheadNPC.query(categoryid, expansion, ptr=ns.ptr))

        for id in force_include:
            if id not in wowhead:
                wowhead[id] = WowheadNPC(id, ptr=ns.ptr)

    defaults = wowhead
    for id, mob in wowdb.items():
        if id in defaults:
            defaults[id].extend(mob)
        else:
            defaults[id] = mob

    write_output("../Data/defaults.lua", defaults, strip=ns.strip_empties)
    print("Defaults written")
