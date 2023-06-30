"""
usage: from sky130_mapped import sky130_mapped_pdk
"""
import sky130

from PDK.mappedpdk import MappedPDK
from pathlib import Path

sky130.PDK.layers["capm3"] = (89, 44)

# use mimcap over metal 3
sky130_glayer_mapping = {
    # copied layers
    "capbottommet": "met3drawing",
    "captopmet": "met4drawing",
    "capvia": "via3drawing",
    # original layers
    "capmet": "capm3",
    "met5": "met4drawing",
    "via4": "via3drawing",
    "met4": "met3drawing",
    "via3": "via2drawing",
    "met3": "met2drawing",
    "via2": "viadrawing",
    "met2": "met1drawing",
    "via1": "mcondrawing",
    "met1": "li1drawing",
    "mcon": "licon1drawing",
    "poly": "polydrawing",
    "active_diff": "diffdrawing",
    "active_tap": "tapdrawing",
    "n+s/d": "nsdmdrawing",
    "p+s/d": "psdmdrawing",
    "nwell": "nwelldrawing",
    "pwell": "pwelldrawing",
    "dnwell": "dnwelldrawing",
}

sky130_lydrc_file_path = Path(__file__).resolve().parent / "sky130.lydrc"


grulesobj = dict()
for glayer in MappedPDK.valid_glayers:
    grulesobj[glayer] = dict((x, None) for x in MappedPDK.valid_glayers)

grulesobj["dnwell"]["dnwell"] = {"min_width": 3.0, "min_separation": 6.3}
grulesobj["dnwell"]["pwell"] = {}
grulesobj["dnwell"]["nwell"] = {"min_separation": 4.5}
grulesobj["dnwell"]["p+s/d"] = {}
grulesobj["dnwell"]["n+s/d"] = {}
grulesobj["dnwell"]["active_diff"] = {}
grulesobj["dnwell"]["active_tap"] = {"min_separation": 0.34}
grulesobj["dnwell"]["poly"] = {}
grulesobj["dnwell"]["mcon"] = {}
grulesobj["dnwell"]["met1"] = {}
grulesobj["dnwell"]["via1"] = {}
grulesobj["dnwell"]["met2"] = {}
grulesobj["dnwell"]["via2"] = {}
grulesobj["dnwell"]["met3"] = {}
grulesobj["dnwell"]["via3"] = {}
grulesobj["dnwell"]["met4"] = {}
grulesobj["pwell"]["dnwell"] = {}
grulesobj["pwell"]["pwell"] = {}
grulesobj["pwell"]["nwell"] = {}
grulesobj["pwell"]["p+s/d"] = {}
grulesobj["pwell"]["n+s/d"] = {}
grulesobj["pwell"]["active_diff"] = {}
grulesobj["pwell"]["active_tap"] = {"min_enclosure": 0.18}
grulesobj["pwell"]["poly"] = {}
grulesobj["pwell"]["mcon"] = {}
grulesobj["pwell"]["met1"] = {}
grulesobj["pwell"]["via1"] = {}
grulesobj["pwell"]["met2"] = {}
grulesobj["pwell"]["via2"] = {}
grulesobj["pwell"]["met3"] = {}
grulesobj["pwell"]["via3"] = {}
grulesobj["pwell"]["met4"] = {}
grulesobj["nwell"]["dnwell"] = {}
grulesobj["nwell"]["pwell"] = {}
grulesobj["nwell"]["nwell"] = {"min_width": 0.84, "min_sepeartion": 1.27}
grulesobj["nwell"]["p+s/d"] = {}
grulesobj["nwell"]["n+s/d"] = {}
grulesobj["nwell"]["active_diff"] = {}
grulesobj["nwell"]["active_tap"] = {"min_enclosure": 0.18}
grulesobj["nwell"]["poly"] = {}
grulesobj["nwell"]["mcon"] = {}
grulesobj["nwell"]["met1"] = {}
grulesobj["nwell"]["via1"] = {}
grulesobj["nwell"]["met2"] = {}
grulesobj["nwell"]["via2"] = {}
grulesobj["nwell"]["met3"] = {}
grulesobj["nwell"]["via3"] = {}
grulesobj["nwell"]["met4"] = {}
grulesobj["p+s/d"]["dnwell"] = {}
grulesobj["p+s/d"]["pwell"] = {}
grulesobj["p+s/d"]["nwell"] = {}
grulesobj["p+s/d"]["p+s/d"] = {"min_width": 0.38, "min_separation": 0.38}
grulesobj["p+s/d"]["n+s/d"] = {}
grulesobj["p+s/d"]["active_diff"] = {"min_enclosure": 0.13, "min_separation": 0.13}
grulesobj["p+s/d"]["active_tap"] = {"min_enclosure": 0.13, "min_separation": 0.13}
grulesobj["p+s/d"]["poly"] = {}
grulesobj["p+s/d"]["mcon"] = {}
grulesobj["p+s/d"]["met1"] = {}
grulesobj["p+s/d"]["via1"] = {}
grulesobj["p+s/d"]["met2"] = {}
grulesobj["p+s/d"]["via2"] = {}
grulesobj["p+s/d"]["met3"] = {}
grulesobj["p+s/d"]["via3"] = {}
grulesobj["p+s/d"]["met4"] = {}
grulesobj["n+s/d"]["dnwell"] = {}
grulesobj["n+s/d"]["pwell"] = {}
grulesobj["n+s/d"]["nwell"] = {}
grulesobj["n+s/d"]["p+s/d"] = {}
grulesobj["n+s/d"]["n+s/d"] = {"min_width": 0.38, "min_separation": 0.38}
grulesobj["n+s/d"]["active_diff"] = {"min_enclosure": 0.13, "min_separation": 0.13}
grulesobj["n+s/d"]["active_tap"] = {"min_enclosure": 0.13, "min_separation": 0.13}
grulesobj["n+s/d"]["poly"] = {}
grulesobj["n+s/d"]["mcon"] = {}
grulesobj["n+s/d"]["met1"] = {}
grulesobj["n+s/d"]["via1"] = {}
grulesobj["n+s/d"]["met2"] = {}
grulesobj["n+s/d"]["via2"] = {}
grulesobj["n+s/d"]["met3"] = {}
grulesobj["n+s/d"]["via3"] = {}
grulesobj["n+s/d"]["met4"] = {}
grulesobj["active_diff"]["dnwell"] = {}
grulesobj["active_diff"]["pwell"] = {}
grulesobj["active_diff"]["nwell"] = {}
grulesobj["active_diff"]["p+s/d"] = {}
grulesobj["active_diff"]["n+s/d"] = {}
grulesobj["active_diff"]["active_diff"] = {"min_width": 0.15, "min_separation": 0.27}
grulesobj["active_diff"]["active_tap"] = {"min_separation": 0.27}
grulesobj["active_diff"]["poly"] = {"overhang": 0.25}
grulesobj["active_diff"]["mcon"] = {"min_enclosure": 0.06}
grulesobj["active_diff"]["met1"] = {}
grulesobj["active_diff"]["via1"] = {}
grulesobj["active_diff"]["met2"] = {}
grulesobj["active_diff"]["via2"] = {}
grulesobj["active_diff"]["met3"] = {}
grulesobj["active_diff"]["via3"] = {}
grulesobj["active_diff"]["met4"] = {}
grulesobj["active_tap"]["dnwell"] = {}
grulesobj["active_tap"]["pwell"] = {}
grulesobj["active_tap"]["nwell"] = {}
grulesobj["active_tap"]["p+s/d"] = {}
grulesobj["active_tap"]["n+s/d"] = {}
grulesobj["active_tap"]["active_diff"] = {}
grulesobj["active_tap"]["active_tap"] = {"min_width": 0.15, "min_separation": 0.27}
grulesobj["active_tap"]["poly"] = {}
grulesobj["active_tap"]["mcon"] = {"min_enclosure": 0.12}
grulesobj["active_tap"]["met1"] = {}
grulesobj["active_tap"]["via1"] = {}
grulesobj["active_tap"]["met2"] = {}
grulesobj["active_tap"]["via2"] = {}
grulesobj["active_tap"]["met3"] = {}
grulesobj["active_tap"]["via3"] = {}
grulesobj["active_tap"]["met4"] = {}
grulesobj["poly"]["dnwell"] = {}
grulesobj["poly"]["pwell"] = {}
grulesobj["poly"]["nwell"] = {}
grulesobj["poly"]["p+s/d"] = {}
grulesobj["poly"]["n+s/d"] = {}
grulesobj["poly"]["active_diff"] = {}
grulesobj["poly"]["active_tap"] = {}
grulesobj["poly"]["poly"] = {
    "min_width": 0.15,
    "min_separation": 0.21,
    "extension": 0.13,
}
grulesobj["poly"]["mcon"] = {"min_enclosure": 0.05, "min_separation": 0.06}
grulesobj["poly"]["met1"] = {}
grulesobj["poly"]["via1"] = {}
grulesobj["poly"]["met2"] = {}
grulesobj["poly"]["via2"] = {}
grulesobj["poly"]["met3"] = {}
grulesobj["poly"]["via3"] = {}
grulesobj["poly"]["met4"] = {}
grulesobj["mcon"]["dnwell"] = {}
grulesobj["mcon"]["pwell"] = {}
grulesobj["mcon"]["nwell"] = {}
grulesobj["mcon"]["p+s/d"] = {}
grulesobj["mcon"]["n+s/d"] = {}
grulesobj["mcon"]["active_diff"] = {}
grulesobj["mcon"]["active_tap"] = {}
grulesobj["mcon"]["poly"] = {}
grulesobj["mcon"]["mcon"] = {"min_width": 0.17, "min_separation": 0.17, "width": 0.17}
grulesobj["mcon"]["met1"] = {"min_enclosure": 0.08}
grulesobj["mcon"]["via1"] = {}
grulesobj["mcon"]["met2"] = {}
grulesobj["mcon"]["via2"] = {}
grulesobj["mcon"]["met3"] = {}
grulesobj["mcon"]["via3"] = {}
grulesobj["mcon"]["met4"] = {}
grulesobj["met1"]["dnwell"] = {}
grulesobj["met1"]["pwell"] = {}
grulesobj["met1"]["nwell"] = {}
grulesobj["met1"]["p+s/d"] = {}
grulesobj["met1"]["n+s/d"] = {}
grulesobj["met1"]["active_diff"] = {}
grulesobj["met1"]["active_tap"] = {}
grulesobj["met1"]["poly"] = {}
grulesobj["met1"]["mcon"] = {}
grulesobj["met1"]["met1"] = {"min_width": 0.17, "min_separation": 0.17}
grulesobj["met1"]["via1"] = {"min_enclosure": 0.0}
grulesobj["met1"]["met2"] = {}
grulesobj["met1"]["via2"] = {}
grulesobj["met1"]["met3"] = {}
grulesobj["met1"]["via3"] = {}
grulesobj["met1"]["met4"] = {}
grulesobj["via1"]["dnwell"] = {}
grulesobj["via1"]["pwell"] = {}
grulesobj["via1"]["nwell"] = {}
grulesobj["via1"]["p+s/d"] = {}
grulesobj["via1"]["n+s/d"] = {}
grulesobj["via1"]["active_diff"] = {}
grulesobj["via1"]["active_tap"] = {}
grulesobj["via1"]["poly"] = {}
grulesobj["via1"]["mcon"] = {}
grulesobj["via1"]["met1"] = {}
grulesobj["via1"]["via1"] = {"min_width": 0.17, "min_separation": 0.19, "width": 0.17}
grulesobj["via1"]["met2"] = {"min_enclosure": 0.06}
grulesobj["via1"]["via2"] = {}
grulesobj["via1"]["met3"] = {}
grulesobj["via1"]["via3"] = {}
grulesobj["via1"]["met4"] = {}
grulesobj["met2"]["dnwell"] = {}
grulesobj["met2"]["pwell"] = {}
grulesobj["met2"]["nwell"] = {}
grulesobj["met2"]["p+s/d"] = {}
grulesobj["met2"]["n+s/d"] = {}
grulesobj["met2"]["active_diff"] = {}
grulesobj["met2"]["active_tap"] = {}
grulesobj["met2"]["poly"] = {}
grulesobj["met2"]["mcon"] = {}
grulesobj["met2"]["met1"] = {}
grulesobj["met2"]["via1"] = {}
grulesobj["met2"]["met2"] = {"min_width": 0.14, "min_separation": 0.14}
grulesobj["met2"]["via2"] = {"min_enclosure": 0.14}
grulesobj["met2"]["met3"] = {}
grulesobj["met2"]["via3"] = {}
grulesobj["met2"]["met4"] = {}
grulesobj["via2"]["dnwell"] = {}
grulesobj["via2"]["pwell"] = {}
grulesobj["via2"]["nwell"] = {}
grulesobj["via2"]["p+s/d"] = {}
grulesobj["via2"]["n+s/d"] = {}
grulesobj["via2"]["active_diff"] = {}
grulesobj["via2"]["active_tap"] = {}
grulesobj["via2"]["poly"] = {}
grulesobj["via2"]["mcon"] = {}
grulesobj["via2"]["met1"] = {}
grulesobj["via2"]["via1"] = {}
grulesobj["via2"]["met2"] = {}
grulesobj["via2"]["via2"] = {"min_width": 0.21, "min_separation": 0.17, "width": 0.15}
grulesobj["via2"]["met3"] = {"min_enclosure": 0.09}
grulesobj["via2"]["via3"] = {}
grulesobj["via2"]["met4"] = {}
grulesobj["met3"]["dnwell"] = {}
grulesobj["met3"]["pwell"] = {}
grulesobj["met3"]["nwell"] = {}
grulesobj["met3"]["p+s/d"] = {}
grulesobj["met3"]["n+s/d"] = {}
grulesobj["met3"]["active_diff"] = {}
grulesobj["met3"]["active_tap"] = {}
grulesobj["met3"]["poly"] = {}
grulesobj["met3"]["mcon"] = {}
grulesobj["met3"]["met1"] = {}
grulesobj["met3"]["via1"] = {}
grulesobj["met3"]["met2"] = {}
grulesobj["met3"]["via2"] = {}
grulesobj["met3"]["met3"] = {"min_width": 0.14, "min_separation": 0.14}
grulesobj["met3"]["via3"] = {}
grulesobj["met3"]["met4"] = {}
grulesobj["via3"]["dnwell"] = {}
grulesobj["via3"]["pwell"] = {}
grulesobj["via3"]["nwell"] = {}
grulesobj["via3"]["p+s/d"] = {}
grulesobj["via3"]["n+s/d"] = {}
grulesobj["via3"]["active_diff"] = {}
grulesobj["via3"]["active_tap"] = {}
grulesobj["via3"]["poly"] = {}
grulesobj["via3"]["mcon"] = {}
grulesobj["via3"]["met1"] = {}
grulesobj["via3"]["via1"] = {}
grulesobj["via3"]["met2"] = {}
grulesobj["via3"]["via2"] = {}
grulesobj["via3"]["met3"] = {}
grulesobj["via3"]["via3"] = {"min_width": 0.2, "min_separation": 0.2, "width": 0.2}
grulesobj["via3"]["met4"] = {"min_enclosure": 0.65}
grulesobj["met4"]["dnwell"] = {}
grulesobj["met4"]["pwell"] = {}
grulesobj["met4"]["nwell"] = {}
grulesobj["met4"]["p+s/d"] = {}
grulesobj["met4"]["n+s/d"] = {}
grulesobj["met4"]["active_diff"] = {}
grulesobj["met4"]["active_tap"] = {}
grulesobj["met4"]["poly"] = {}
grulesobj["met4"]["mcon"] = {}
grulesobj["met4"]["met1"] = {}
grulesobj["met4"]["via1"] = {}
grulesobj["met4"]["met2"] = {}
grulesobj["met4"]["via2"] = {}
grulesobj["met4"]["met3"] = {}
grulesobj["met4"]["via3"] = {}
grulesobj["met4"]["met4"] = {"min_width": 0.3, "min_separation": 0.3}

sky130_mapped_pdk = MappedPDK.from_gf_pdk(
    sky130.PDK,
    sky130_glayer_mapping,
    grules=grulesobj,
    klayout_lydrc_file=sky130_lydrc_file_path,
)
