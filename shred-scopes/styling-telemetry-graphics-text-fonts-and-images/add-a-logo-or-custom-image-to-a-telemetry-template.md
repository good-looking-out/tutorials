# How to Add a Logo or Custom Image to a Telemetry Template

An image layer can place a logo, badge, sponsor mark, decorative panel, or other custom graphic inside a Shred Scopes telemetry template. The image can be uploaded to the account before editing, or dragged from the computer directly into the Template Editor.

Use an image that the video creator is authorized to reproduce. A PNG is appropriate when transparent areas must remain transparent. A JPEG can be suitable for a rectangular photograph or other fully opaque image.

## Prepare the image

Before uploading, check that:

- The image is a PNG or JPEG.
- Its dimensions are large enough for its intended export size.
- A transparent logo actually contains transparency and is saved as PNG.
- Unnecessary empty space around the visible artwork has been removed.
- The file is not much larger than the overlay requires.
- Its colors will remain recognizable over the source footage.

A tightly cropped source is easier to position and scale than a logo surrounded by a large transparent border.

## 1. Upload the image to the account

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and open the media-management area. Choose "Manage Image Assets."

Start the upload workflow, then:

1. Select the file under "PNG or JPEG source image."
2. Enter a recognizable "Image name."
3. Choose the appropriate "Image type."
4. Mark the image as a favorite if it should be easier to find later.
5. Start the upload.
6. Keep the page open until the upload reports completion.

The uploaded image becomes available to image layers in custom templates.

## 2. Open the template

Load the intended telemetry source and open the Template Editor. Choose an existing custom template, create a new template, or use "Template" > "Save As New" to create a custom copy of a built-in design.

Confirm the template canvas dimensions before placing the image. Position and size values are relative to that canvas.

## 3. Add an image layer

In "Layers":

1. Select "Add Layer" or a plus control labeled "Add layer here."
2. Choose the "image" layer type.
3. Choose the uploaded image.
4. Add the layer and give it a descriptive name, such as "Event logo."

The image summary shows identifying information about the selected asset, including its name, dimensions, crop state, and availability. Review this summary if the wrong asset appears.

An image can also be dragged from the computer into the Template Editor. This creates an image layer directly. Confirm its upload status before relying on it in templates used from another session or browser.

## 4. Restore the source proportions

Choose "Reset to Natural" when the image appears stretched or its starting size is unsuitable. This restores the source or cropped aspect ratio and fits the image within the canvas.

Then adjust width and height. Preserve the aspect ratio for logos unless intentional distortion is part of the design. If the interface allows the dimensions to change independently, verify circles, lettering, and brand marks for stretching.

## 5. Choose the fit and crop

Use "Fit" to control how the image occupies its layer bounds. The appropriate setting depends on whether the complete source must remain visible or whether the bounds should be filled.

Use "Crop Image" when only part of the uploaded image should appear. Confirm the crop, then reposition and resize the layer. Use "Undo Crop" to return to the uncropped source if the result is incorrect.

Cropping the layer does not require editing the original file on the computer, but a clean source crop can still make repeated use easier.

## 6. Position and transform the image

Configure:

- Width and height
- X and Y position
- Rotation
- Horizontal or vertical flip where needed
- Uniform or individual corner radius where available

Use alignment controls and guides to place the image consistently with nearby telemetry. Keep it inside the template canvas because content outside the canvas will not appear in the exported overlay.

For a small logo, preview at the final output scale. Thin lettering can become unreadable after video compression.

## 7. Style the image layer

Use "Opacity" to fade the complete image. A partially transparent decorative image can sit behind telemetry, but an important logo may need higher opacity.

Use "Blend mode" only after checking normal compositing. Blend results depend on the layers and source imagery underneath, so inspect several representative video frames.

Supported image controls can also provide:

- Corner rounding
- Shadow or glow color, opacity, blur, distance, and angle
- High-quality smoothing

Keep high-quality smoothing enabled for photographs and scaled logos. Turn it off only when hard pixel edges are intentionally required.

## 8. Clip the image with a shape

Enable shape clipping when the image should appear inside a circle, rounded panel, or another compatible static shape.

Choose the intended clipping layer and confirm that it remains aligned with the image. The clipping shape determines which image area remains visible. If the image disappears, check the shape's position, size, compatibility, and layer relationship.

## 9. Arrange the layer order

Move the image to the correct front-to-back position:

- Put a logo above a background plate when it must remain fully visible.
- Put a decorative image below data text and tick labels.
- Keep a clipping shape aligned with the image it controls.
- Lock the image layer after final placement to avoid accidental movement.

Preview the complete template rather than judging the image by itself.

## 10. Save and test the asset reference

Save the custom template, then place it over the source in Source Composite. Check bright and dark frames, motion, canvas edges, opacity, and the final output size.

The saved template refers to the account image; it does not contain a separate embedded copy. Do not delete the image asset while a saved template still depends on it. Reopen the template after saving to confirm that the image remains available.
