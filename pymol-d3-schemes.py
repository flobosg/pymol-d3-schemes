from pymol import cmd

def hex_to_rgb(hex_str):
    return [int(hex_str.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)]

schemes = {
    "Blues": ["#f7fbff","#e3eef9","#cfe1f2","#b5d4e9","#93c3df","#6daed5","#4b97c9","#2f7ebc","#1864aa","#0a4a90","#08306b"],
    "Greens": ["#f7fcf5","#e8f6e3","#d3eecd","#b7e2b1","#97d494","#73c378","#4daf62","#2f984f","#157f3b","#036429","#00441b"],
    "Greys": ["#ffffff","#f2f2f2","#e2e2e2","#cecece","#b4b4b4","#979797","#7a7a7a","#5f5f5f","#404040","#1e1e1e","#000000"],
    "Oranges": ["#fff5eb","#fee8d3","#fdd8b3","#fdc28c","#fda762","#fb8d3d","#f2701d","#e25609","#c44103","#9f3303","#7f2704"],
    "Purples": ["#fcfbfd","#f1eff6","#e2e1ef","#cecee5","#b6b5d8","#9e9bc9","#8782bc","#7363ac","#61409b","#501f8c","#3f007d"],
    "Reds": ["#fff5f0","#fee3d6","#fdc9b4","#fcaa8e","#fc8a6b","#f9694c","#ef4533","#d92723","#bb151a","#970b13","#67000d"],
    "BuGn": ["#f7fcfd","#e8f6f9","#d5efed","#b7e4da","#8fd3c1","#68c2a3","#49b17f","#2f9959","#157f3c","#036429","#00441b"],
    "BuPu": ["#f7fcfd","#e4eef5","#ccddec","#b2cae1","#9cb3d5","#8f95c6","#8c74b5","#8952a5","#852d8f","#730f71","#4d004b"],
    "GnBu": ["#f7fcf0","#e5f5df","#d3eece","#bde5bf","#9ed9bb","#7bcbc4","#58b7cd","#399cc6","#1d7eb7","#0b60a1","#084081"],
    "OrRd": ["#fff7ec","#feebcf","#fddcaf","#fdca94","#fdb07a","#fa8e5d","#f16c49","#e04530","#c81d13","#a70403","#7f0000"],
    "PuBuGn": ["#fff7fb","#efe7f2","#dbd8ea","#bec9e2","#98b9d9","#69a8cf","#4096c0","#19879f","#037877","#016353","#014636"],
    "PuBu": ["#fff7fb","#efeaf4","#dbdaeb","#bfc9e2","#9bb9d9","#72a8cf","#4394c3","#1a7db6","#0667a1","#045281","#023858"],
    "PuRd": ["#f7f4f9","#eae3f0","#dcc9e2","#d0aad2","#d08ac2","#dd63ae","#e33890","#d71c6c","#b70b4f","#8f023a","#67001f"],
    "RdPu": ["#fff7f3","#fde4e1","#fccfcc","#fbb5bc","#f993b0","#f369a3","#e03e98","#c01788","#99037c","#700174","#49006a"],
    "YlGnBu": ["#ffffd9","#eff9bd","#d5eeb3","#a9ddb7","#73c9bd","#45b4c2","#2897bf","#2073b2","#234ea0","#1c3185","#081d58"],
    "YlGn": ["#ffffe5","#f7fcc4","#e4f4ac","#c7e89b","#a2d88a","#78c578","#4eaf63","#2f944e","#15793f","#036034","#004529"],
    "YlOrBr": ["#ffffe5","#fff8c4","#feeaa1","#fed676","#feba4a","#fb992c","#ee7918","#d85b0a","#b74304","#8f3204","#662506"],
    "YlOrRd": ["#ffffcc","#fff0a9","#fee087","#fec965","#feab4b","#fd893c","#fa5c2e","#ec3023","#d31121","#af0225","#800026"],
    "Cividis": ["#002051","#0a326a","#2b446e","#4d566d","#696970","#7f7c75","#948f78","#ada476","#caba6a","#ead156","#fdea45"],
    "Viridis": ["#440154","#482475","#414487","#355f8d","#2a788e","#21918c","#22a884","#44bf70","#7ad151","#bddf26","#fde725"],
    "Inferno": ["#000004","#160b39","#420a68","#6a176e","#932667","#bc3754","#dd513a","#f37819","#fca50a","#f6d746","#fcffa4"],
    "Magma": ["#000004","#140e36","#3b0f70","#641a80","#8c2981","#b73779","#de4968","#f7705c","#fe9f6d","#fecf92","#fcfdbf"],
    "Plasma": ["#0d0887","#41049d","#6a00a8","#8f0da4","#b12a90","#cc4778","#e16462","#f2844b","#fca636","#fcce25","#f0f921"],
    "Warm": ["#6e40aa","#963db3","#bf3caf","#e4419d","#fe4b83","#ff5e63","#ff7847","#fb9633","#e2b72f","#c6d63c","#aff05b"],
    "Cool": ["#6e40aa","#6054c8","#4c6edb","#368ce1","#23abd8","#1ac7c2","#1ddfa3","#30ef82","#52f667","#7ff658","#aff05b"],
    "CubehelixDefault": ["#000000","#1a1530","#163d4e","#1f6642","#54792f","#a07949","#d07e93","#cf9cda","#c1caf3","#d2eeef","#ffffff"],
    "Turbo": ["#23171b","#4a58dd","#2f9df5","#27d7c4","#4df884","#95fb51","#dedd32","#ffa423","#f65f18","#ba2208","#900c00"],
    "BrBG": ["#543005","#8c510a","#bf812d","#dfc27d","#f6e8c3","#f5f5f5","#c7eae5","#80cdc1","#35978f","#01665e","#003c30"],
    "PRGn": ["#40004b","#762a83","#9970ab","#c2a5cf","#e7d4e8","#f7f7f7","#d9f0d3","#a6dba0","#5aae61","#1b7837","#00441b"],
    "PiYG": ["#8e0152","#c51b7d","#de77ae","#f1b6da","#fde0ef","#f7f7f7","#e6f5d0","#b8e186","#7fbc41","#4d9221","#276419"],
    "PuOr": ["#2d004b","#542788","#8073ac","#b2abd2","#d8daeb","#f7f7f7","#fee0b6","#fdb863","#e08214","#b35806","#7f3b08"],
    "RdBu": ["#67001f","#b2182b","#d6604d","#f4a582","#fddbc7","#f7f7f7","#d1e5f0","#92c5de","#4393c3","#2166ac","#053061"],
    "RdGy": ["#67001f","#b2182b","#d6604d","#f4a582","#fddbc7","#ffffff","#e0e0e0","#bababa","#878787","#4d4d4d","#1a1a1a"],
    "RdYlBu": ["#a50026","#d73027","#f46d43","#fdae61","#fee090","#ffffbf","#e0f3f8","#abd9e9","#74add1","#4575b4","#313695"],
    "RdYlGn": ["#a50026","#d73027","#f46d43","#fdae61","#fee08b","#ffffbf","#d9ef8b","#a6d96a","#66bd63","#1a9850","#006837"],
    "Spectral": ["#9e0142","#d53e4f","#f46d43","#fdae61","#fee08b","#ffffbf","#e6f598","#abdda4","#66c2a5","#3288bd","#5e4fa2"],
    "Rainbow": ["#6e40aa","#bf3caf","#fe4b83","#ff7847","#e2b72f","#aff05b","#52f667","#1ddfa3","#23abd8","#4c6edb","#6e40aa"],
    "Sinebow": ["#ff4040","#e78d0b","#a7d503","#58fc2a","#18f472","#00bfbf","#1872f4","#582afc","#a703d5","#e70b8d","#ff4040"],
    "Category10": ["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b","#e377c2","#7f7f7f","#bcbd22","#17becf"],
    "Accent": ["#7fc97f","#beaed4","#fdc086","#ffff99","#386cb0","#f0027f","#bf5b17","#666666"],
    "Dark2": ["#1b9e77","#d95f02","#7570b3","#e7298a","#66a61e","#e6ab02","#a6761d","#666666"],
    "Paired": ["#a6cee3","#1f78b4","#b2df8a","#33a02c","#fb9a99","#e31a1c","#fdbf6f","#ff7f00","#cab2d6","#6a3d9a","#ffff99","#b15928"],
    "Pastel1": ["#fbb4ae","#b3cde3","#ccebc5","#decbe4","#fed9a6","#ffffcc","#e5d8bd","#fddaec","#f2f2f2"],
    "Pastel2": ["#b3e2cd","#fdcdac","#cbd5e8","#f4cae4","#e6f5c9","#fff2ae","#f1e2cc","#cccccc"],
    "Set1": ["#e41a1c","#377eb8","#4daf4a","#984ea3","#ff7f00","#ffff33","#a65628","#f781bf","#999999"],
    "Set2": ["#66c2a5","#fc8d62","#8da0cb","#e78ac3","#a6d854","#ffd92f","#e5c494","#b3b3b3"],
    "Set3": ["#8dd3c7","#ffffb3","#bebada","#fb8072","#80b1d3","#fdb462","#b3de69","#fccde5","#d9d9d9","#bc80bd","#ccebc5","#ffed6f"],
    "Tableau10": ["#4e79a7","#f28e2c","#e15759","#76b7b2","#59a14f","#edc949","#af7aa1","#ff9da7","#9c755f","#bab0ab"]
}

for k in schemes.keys():
    for i, color in enumerate(schemes[k], 1):
        cmd.set_color(f"d3{k}-{i}", hex_to_rgb(color))
