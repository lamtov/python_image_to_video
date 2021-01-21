import comtypes.client as ct
psApp = ct.CreateObject('Photoshop.Application', dynamic=True)
psApp.Visible = True
image_t_shirt=r"C:\Users\Lam\Pictures\BlueStacks\447857-PF1FKN-86-02.png"
target = psApp.Open(image_t_shirt)

target_layer = target.ArtLayers.Item(1)
target_layer.Copy()



psApp.Open(r"C:\Users\Lam\Pictures\BlueStacks\t-shirt-mock-up-design\OJYV111.psd")
psDoc=psApp.Application.ActiveDocument
layer=psDoc.ArtLayers.Item(1)
psDoc.activeLayer = psDoc.ArtLayers.Item(1)
psApp.executeAction(psApp.stringIDToTypeID("placedLayerEditContents"))
# psApp.executeAction(psApp.stringIDToTypeID("placedLayerEditContents"))
smartDoc = psApp.activeDocument

smartDoc.Paste()
psApp.activeDocument.save()
psApp.activeDocument.close()