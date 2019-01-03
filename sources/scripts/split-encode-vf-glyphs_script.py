#MenuTitle: Prep Designspace Encode Sans
# -*- coding: utf-8 -*-
"""
    Makes a copy of a GlyphsApp source, with adjustments to designspace by:
    - making masters from interpolated normal-width light and bold instances
    - deleting wide and condensed masters

    Specific to Encode Sans for now. Assumes:
    - "Width" is the second axis
    - Normal-width instances are given "Width" axes value of 500
    - Instances are sorted by weight, with lightest and boldest at each end

    To use, symlink this script into glyphs script folder with:

    ln -s THIS/PATH/sources/scripts/helpers/split-encode-vf-glyphs_script.py GLYPHS/SCRIPTS/PATH/prep-designspace-glyphs_script.py
"""

font = Glyphs.font

normalWidthValue = 500

widthAxisIndex = 1


# ============================================================================
# delete non-normal width instances ==========================================

instancesToRemove = []

for index, instance in enumerate(font.instances):
    if instance.axes[widthAxisIndex] != normalWidthValue:
        instancesToRemove.append(index)

instancesToRemove = sorted(instancesToRemove)

for instanceIndex in instancesToRemove[::-1]:
    print(instanceIndex)
    del font.instances[instanceIndex]



# ============================================================================
# make masters from instance designspace corners =============================

print("Making masters from normal-width corner instances:")

def copyFromInterpolatedFont(instanceIndex):
    instanceFont = font.instances[instanceIndex].interpolatedFont

    instanceFontMasterID = instanceFont.masters[0].id

    font.masters.append(instanceFont.masters[0])
    newMasterID = instanceFontMasterID # these are the same; copying for clarity below

    print("\n=================================")
    print("Instance Weight: " + str(font.instances[instanceIndex].weightValue))

    # copy glyphs from instance font to new master
    for index,glyph in enumerate(font.glyphs): # (you can use font.glyphs()[:10] to do the first 10 glyphs only while making/testing script)
        instanceGlyph = instanceFont.glyphs[index] # make variable for glyph of interpolated font
        glyph.layers[instanceFontMasterID] = instanceGlyph.layers[instanceFontMasterID]

    # bring kerning in from interpolated font # not yet working
    font.kerning[instanceFontMasterID] = instanceFont.kerning[instanceFontMasterID]

copyFromInterpolatedFont(0)
copyFromInterpolatedFont(-1)

# ============================================================================
# remove old masters and update axis values ==================================

# deletes masters that aren't the normal width – would need more flexibility to be abstracted to other fonts

mastersToDelete = []

for index, master in enumerate(font.masters):
    print(master.axes[widthAxisIndex])
    # round this axis value, because it might interpolate to be very slightly different
    if round(master.axes[widthAxisIndex]) != normalWidthValue:
        mastersToDelete.append(index)

print(mastersToDelete)

for masterIndex in mastersToDelete[::-1]:
    print(font.masters[masterIndex])
    font.removeFontMasterAtIndex_(masterIndex)


# # ============================================================================
# # set varfont axes ===========================================================


fontAxes = [
	{"Name": "Weight", "Tag": "wght"}
]
Font.customParameters["Axes"] = fontAxes

# ============================================================================
# round all coordinates ======================================================

for glyph in font.glyphs:
    for layer in glyph.layers:
        for path in layer.paths:
            for node in path.nodes:
                node.position.x = round(node.position.x)
                node.position.y = round(node.position.y)
        for anchor in layer.anchors:
            anchor.x = round(anchor.x)
            anchor.y = round(anchor.y)
    

# ============================================================================
# save as "build" file =======================================================


buildreadyFolder = 'split'
buildreadySuffix = 'normal_width'

fontPath = font.filepath

if buildreadyFolder not in fontPath:    
    fontPathHead = os.path.split(fontPath)[0] # file folder
    fontPathTail = os.path.split(fontPath)[1] # file name
    buildreadyPathHead = fontPathHead + "/" + buildreadyFolder + "/"

    if os.path.exists(buildreadyPathHead) == False:
        os.mkdir(buildreadyPathHead)

    buildPath = buildreadyPathHead + fontPathTail.replace(".glyphs", "-" + buildreadySuffix + ".glyphs")

else:
    buildPath = fontPath.replace(".glyphs", "-" + buildreadySuffix + ".glyphs")

font.save(buildPath)

# # close original without saving
font.close()

Glyphs.open(buildPath)

