-- DO NOT EDIT THIS FILE; run dataminer.lua to regenerate.
local core = LibStub("AceAddon-3.0"):GetAddon("SilverDragon")
local module = core:NewModule("Data_Wrath")

function module:OnInitialize()
	core:RegisterMobData("Wrath", {
		[32357] = {name="Old Crystalbark",locations={[114]={21002840,22003340,27003560,34002420,35402940},},},
		[32358] = {name="Fumblub Gearwind",locations={[114]={59801460,59802540,62603480,68001920,68403660,73603260},},},
		[32361] = {name="Icehorn",locations={[114]={80404600,81203160,88203960,91403240},},tameable=true,},
		[32377] = {name="Perobas the Bloodthirster",locations={[117]={49800460,52801160,60802000,68201720},},},
		[32386] = {name="Vigdis the War Maiden",locations={[117]={68604840,69405820,73403980,74004500,74005240,74406060},},},
		[32398] = {name="King Ping",locations={[117]={26006380,30807120,31205660,33208020},},},
		[32400] = {name="Tukemuth",locations={[115]={54405540,57004980,59204240,60603020,61805660,62605100,66803280,68004600,68805780,70005140},},},
		[32409] = {name="Crazed Indu'le Survivor",locations={[115]={15405820,15604560,20605520,28406140},},},
		[32417] = {name="Scarlet Highlord Daion",locations={[115]={69207480,71002220,75202760,85803660},},},
		[32422] = {name="Grocklar",locations={[116]={10603920,11207100,12005560,12204440,12805000,17207040,20605620,22407320,28004180},},},
		[32429] = {name="Seething Hate",locations={[116]={28004540,34004920,39605060},},},
		[32435] = {name="Vern",locations={[126]={51203140,57003080},},tameable=true,},
		[32438] = {name="Syreian the Bonecarver",locations={[116]={62803700,65202940,71603500,74204240},},},
		[32447] = {name="Zul'drak Sentinel",locations={[121]={21208260,26208280,28807220,40405460,40406000,42607060,45806040,45807580,49808240},},},
		[32471] = {name="Griegen",locations={[121]={14405620,17407020,20807880,22406180,26205560,26607100},},},
		[32475] = {name="Terror Spinner",locations={[120]={71607500},[121]={53203140,61203640,71402320,71402900,74406640,77204220,81403440},},tameable=true,},
		[32481] = {name="Aotona",locations={[119]={40205900,41206840,42007380,42205180,52407240,54405180,56406520},},tameable=true,},
		[32485] = {name="King Krush",locations={[119]={25804880,29204220,32603540,36202960,47004340,50808140,52204240,58808180,63808280},},tameable=true,},
		[32487] = {name="Putridus the Ancient",locations={[118]={44005820,45205020,49004280,54004120,60804120,65004740,66205260,67405820,68406420},},},
		[32491] = {name="Time-Lost Proto-Drake",locations={[120]={27205660,28405140,31006940,31603800,35607660,36606980,39408440,40205980,50004800},},mount=true,},
		[32495] = {name="Hildana Deathstealer",locations={[118]={28604540,29603800,30803280,36802540,54005300,59605940},},},
		[32500] = {name="Dirkee",locations={[120]={37805840,41005180,41404020,68004760},},},
		[32501] = {name="High Thane Jorfus",locations={[118]={31206220,33607060,47407820,48408500,67603860,72803500},},},
		[32517] = {name="Loque'nahak",locations={[119]={20607000,30806640,35402960,50808120,58402140,66007900,70807120},},tameable=true,},
		[32630] = {name="Vyragosa",locations={[120]={26405980,26407160,26604320,28406520,31203800,31404860,36207740,36807140,38406000,40208440,44203100,47608160,48406640,48803760,49407200,51803060},},},
		[33776] = {name="Gondria",locations={[121]={61006160,63204340,67607740,69404800,77006940},},tameable=true,},
		[35189] = {name="Skoll",locations={[120]={27805040,30206460,46206440},},tameable=true,},
		[38453] = {name="Arcturis",locations={[116]={31005580},},tameable=true,},
	})
end
