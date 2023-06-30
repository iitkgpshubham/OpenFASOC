# TODO: gf180 mimcap generator
"""
usage: from gf180_mapped import gf180_mapped_pdk
"""

from gf180.layers import LAYER  # , LAYER_VIEWS

from PDK.mappedpdk import MappedPDK
from pathlib import Path


gf180_glayer_mapping = {
    "met5": "metal5",
    "via4": "via4",
    "met4": "metal4",
    "via3": "via3",
    "met3": "metal3",
    "via2": "via2",
    "met2": "metal2",
    "via1": "via1",
    "met1": "metal1",
    "mcon": "contact",
    "poly": "poly2",
    "active_diff": "comp",
    "active_tap": "comp",
    "n+s/d": "nplus",
    "p+s/d": "pplus",
    "nwell": "nwell",
    "pwell": "lvpwell",
    "dnwell": "dnwell",
}

# note for DRC, there is mim_option 'A' which runs by default or mim_option 'B'

gf180_lydrc_file_path = Path(__file__).resolve().parent / "gf180mcu_drc.lydrc"

grulesobj = dict()
for glayer in MappedPDK.valid_glayers:
    grulesobj[glayer] = dict((x, None) for x in MappedPDK.valid_glayers)

grulesobj["dnwell"]["dnwell"] = {"min_width": 1.7, "min_separation": 5.42}
grulesobj["dnwell"]["pwell"] = {"min_enclosure": 2.5}
grulesobj["dnwell"]["nwell"] = {"min_separation": 3.1, "min_enclosure": 0.5}
grulesobj["dnwell"]["p+s/d"] = {}
grulesobj["dnwell"]["n+s/d"] = {}
grulesobj["dnwell"]["active_diff"] = {"min_enclosure": 0.93}
grulesobj["dnwell"]["active_tap"] = {"min_enclosure": 0.62, "min_separation": 2.5}
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
grulesobj["pwell"]["pwell"] = {"min_width": 0.6, "min_separation": 1.4}
grulesobj["pwell"]["nwell"] = {"min_separation": 0.0}
grulesobj["pwell"]["p+s/d"] = {}
grulesobj["pwell"]["n+s/d"] = {}
grulesobj["pwell"]["active_diff"] = {"min_enclosure": 0.43}
grulesobj["pwell"]["active_tap"] = {"min_enclosure": 0.12}
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
grulesobj["nwell"]["nwell"] = {"min_width": 0.86, "min_separation": 1.4}
grulesobj["nwell"]["p+s/d"] = {}
grulesobj["nwell"]["n+s/d"] = {}
grulesobj["nwell"]["active_diff"] = {"min_enclosure": 0.43}
grulesobj["nwell"]["active_tap"] = {"min_enclosure": 0.12}
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
grulesobj["p+s/d"]["p+s/d"] = {"min_width": 0.4, "min_separation": 0.4}
grulesobj["p+s/d"]["n+s/d"] = {}
grulesobj["p+s/d"]["active_diff"] = {}
grulesobj["p+s/d"]["active_tap"] = {"min_enclosure": 0.16}
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
grulesobj["n+s/d"]["n+s/d"] = {"min_width": 0.4, "min_separation": 0.4}
grulesobj["n+s/d"]["active_diff"] = {}
grulesobj["n+s/d"]["active_tap"] = {"min_enclosure": 0.16}
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
grulesobj["active_diff"]["p+s/d"] = {"min_enclosure": 0.23}
grulesobj["active_diff"]["n+s/d"] = {"min_enclosure": 0.23}
grulesobj["active_diff"]["active_diff"] = {"min_width": 0.22, "min_separation": 0.28}
grulesobj["active_diff"]["active_tap"] = {
    "0.3)": "*****FIXTHIS!!!MANUALLY!*****",
    "min_separation": 0.28,
    "max_separation": 20.0,
}
grulesobj["active_diff"]["poly"] = {"overhang": 0.24, "min_separation": 0.1}
grulesobj["active_diff"]["mcon"] = {"min_enclosure": 0.07}
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
grulesobj["active_tap"]["active_tap"] = {"min_width": 0.22, "min_separation": 0.28}
grulesobj["active_tap"]["poly"] = {"min_separation": 0.1}
grulesobj["active_tap"]["mcon"] = {"min_enclosure": 0.07}
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
grulesobj["poly"]["poly"] = {"min_width": 0.28}
grulesobj["poly"]["mcon"] = {"min_enclosure": 0.07, "min_separation": 0.17}
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
grulesobj["mcon"]["mcon"] = {"min_separation": 0.28, "width": 0.22}
grulesobj["mcon"]["met1"] = {"min_enclosure": 0.12}
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
grulesobj["met1"]["met1"] = {"min_width": 0.23, "min_separation": 0.3}
grulesobj["met1"]["via1"] = {"min_enclosure": 0.12}
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
grulesobj["via1"]["via1"] = {"width": 0.26, "min_separation": 0.36}
grulesobj["via1"]["met2"] = {"min_enclosure": 0.12}
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
grulesobj["met2"]["met2"] = {"min_width": 0.28, "min_separation": 0.3}
grulesobj["met2"]["via2"] = {"min_enclosure": 0.12}
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
grulesobj["via2"]["via2"] = {"width": 0.26, "min_separation": 0.36}
grulesobj["via2"]["met3"] = {"min_enclosure": 0.12}
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
grulesobj["met3"]["met3"] = {"min_width": 0.28, "min_separation": 0.3}
grulesobj["met3"]["via3"] = {"min_enclosure": 0.12}
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
grulesobj["via3"]["via3"] = {"width": 0.26, "min_separation": 0.36}
grulesobj["via3"]["met4"] = {"min_enclosure": 0.12}
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
grulesobj["met4"]["met4"] = {"min_width": 0.28, "min_separation": 0.3}


gf180_mapped_pdk = MappedPDK(
    name="gf180",
    glayers=gf180_glayer_mapping,
    layers=LAYER.dict(),
    klayout_lydrc_file=gf180_lydrc_file_path,
    grules=grulesobj,
)
