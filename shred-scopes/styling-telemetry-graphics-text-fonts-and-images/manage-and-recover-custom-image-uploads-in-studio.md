# How to Manage and Recover Custom Image Uploads in Studio

Custom image assets used by Shred Scopes templates are managed separately from the templates that reference them. The image library provides controls for reviewing, renaming, favoriting, and deleting account images, while each image layer provides controls for choosing, replacing, relinking, or recovering its selected asset.

Understanding that relationship helps prevent a saved logo or image layer from becoming unavailable.

## Open the image library

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and open the media-management area. Choose "Manage Image Assets."

Each image card provides a preview and its available management actions. Use the preview and name together to distinguish similar versions.

## Review an uploaded image

Before using an asset, confirm:

- The preview displays the correct PNG or JPEG.
- The image has a clear, unique name.
- The intended image type is selected.
- The upload completed rather than remaining interrupted.
- The image is marked as a favorite if it should be easier to locate.

Rename the asset through "Image name" when its current name is ambiguous. Renaming helps identify it in the picker without changing the visible pixels.

## Complete a new upload

Start the image-upload action, select the file under "PNG or JPEG source image," enter the image name and type, and begin the upload. Keep the page open until completion.

If the connection is interrupted, return to the image library and review the reported status before starting a duplicate upload. Shred Scopes can check an incomplete upload and attempt recovery or cleanup instead of presenting it as a finished asset.

## Inspect an image from its template layer

Open the relevant custom template in the Template Editor and select its image layer. The image summary can show the selected asset's name, dimensions, crop state, account-upload state, and availability.

Use the summary to distinguish among these situations:

- The correct account asset is available.
- A local image is present in the current browser session but has not completed its account upload.
- The saved template points to an asset that can no longer be found.
- The layer is linked to the wrong image.

Do not delete and recreate the layer until the image-specific recovery controls have been reviewed.

## Retry an interrupted account upload

If the layer shows an incomplete or failed account upload:

1. Keep the original browser session open if possible.
2. Select the image layer.
3. Choose "Retry Account Upload."
4. Wait for the status to update.
5. Save the custom template after the account asset becomes available.
6. Reopen the template to verify that the reference resolves.

A successful retry makes the image suitable for later account-backed use. Verify it before closing the only session that still has the local source.

## Keep an image local only

"Keep Local Only" stops the account-upload retry while retaining the current local image in the active browser session.

Use this only for temporary work that will remain in the same session. A local-only image should not be treated as a durable template asset: another browser, another computer, or a later session may not have it.

For a reusable saved template, complete the account upload and verify the saved reference.

## Cancel an upload

Choose "Cancel Account Upload" when the selected file should not be uploaded. Then choose a different image or remove the image layer if it is no longer needed.

Canceling the upload does not automatically make another account asset take its place. Review the layer before saving.

## Replace or relink a missing image

If a saved template opens with an unavailable image:

1. Select the affected image layer.
2. Choose "Choose Image," "Replace Image," or "Relink Image," according to the state shown.
3. Select the correct available account asset, or upload the replacement first.
4. Review the image summary.
5. Use "Reset to Natural" if the replacement has a different aspect ratio.
6. Recheck its crop, fit, width, height, position, corner radius, clipping, opacity, and blend mode.
7. Save the custom template.
8. Reopen it and confirm that the image loads.

A replacement with different dimensions can alter the visible composition even when the layer keeps its previous bounds.

## Recover from an incorrect crop

Choose "Undo Crop" to restore the uncropped source when the image was cropped incorrectly. Use "Crop Image" to make a new crop, then check the result at several output sizes.

Choose "Reset to Natural" if the current dimensions stretch the uncropped or newly cropped image. This restores its natural aspect ratio and fits it inside the canvas.

## Delete an image safely

Deleting an account image is permanent. A saved custom template stores a reference to the asset rather than embedding an independent copy. Deleting the image can therefore leave every template that uses it in a missing-image state.

Before deletion:

1. Identify the custom templates that use the asset.
2. Open each affected image layer.
3. Replace or relink it to the intended alternative.
4. Save each template.
5. Reopen the templates and verify the replacement.
6. Return to "Manage Image Assets."
7. Delete the old image only after no required template depends on it.

If the asset might be needed later, retain it with a clear name rather than deleting it solely to reduce visual clutter.

## Avoid duplicate and ambiguous assets

Use descriptive names that include a useful distinction, such as event, color, or revision. Review the existing library before retrying a new upload, and remove obsolete duplicates only after their template references have been replaced.

Favoriting an image can make a frequently used asset easier to find without creating another copy.

## Verify the repaired template

After any retry, replacement, relink, crop change, or deletion, open each affected template and preview it over representative source footage. Confirm that the image loads, remains proportioned correctly, stays inside the canvas, and retains its intended opacity, blend, clipping, and layer order.

Save only after the image summary and canvas both show the intended account asset.
