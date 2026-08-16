# How to Move, Scale, and Rotate Telemetry Overlay Layers

The Template Editor provides direct canvas manipulation and numeric geometry controls for positioning overlay elements. The available transform controls depend on the layer type: some elements have width and height, some have a radius or endpoints, and nested templates have a uniform "Scale" control.

Use direct manipulation for broad layout work and numeric controls or keyboard nudges for precise placement.

## Open the template for editing

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," load a source, and choose the template.

If the starting design is built in, use "Template" > "Save As New" before relying on the changes for later work.

## Select the intended layer

Select a layer on the canvas or in the "Layers" list. A selected layer displays the handles or bounds supported by that element.

When several layers overlap:

1. Right-click the overlap.
2. Open "Select layer."
3. Choose the required layer by name.

Renaming layers makes this selection process more reliable.

## Move a layer by dragging

Drag an unlocked selected layer to a new canvas position. Use preview zoom to make small elements easier to select, but remember that zoom changes only the on-screen view and not the template's exported size.

After dragging, inspect the layer's position controls. Depending on its type, these can appear as:

- X and Y
- Center X and Center Y
- cx and cy
- Endpoint positions such as x1, y1, x2, and y2

These values refer to the layer's own geometry. A text anchor and a rectangle's upper-left position do not necessarily describe the same visible point.

## Nudge a layer precisely

With the layer selected:

- Press an arrow key to move it by 1 pixel.
- Press Shift plus an arrow key to move it by 10 pixels.

Keyboard nudges are useful for final spacing after a drag. If the arrow keys affect the timeline instead, return focus to the canvas selection before nudging.

## Resize or scale the layer

Drag a supported resize handle for visual adjustment, or edit the layer's geometry controls for exact dimensions.

Common size controls include:

- Width and height for rectangles, images, grids, and many graphics
- Radius for circles, arcs, radial ticks, and circular graphics
- Length for linear ticks and line-based graphics
- Font size or a fitting mode for text
- Scale for a nested template
- Endpoint coordinates for lines and related shapes

Not every layer has a single uniform scale value. Changing width without height can intentionally stretch some geometry, while a nested template's "Scale" enlarges or reduces the complete child design uniformly.

Check stroke widths, text sizes, and tick lengths after a large resize. Those properties may need separate adjustment to maintain the intended visual weight.

## Rotate a layer

Use the canvas rotation handle when the selected layer supports it, or enter a value in its "Rotation" control.

Rotation occurs around the origin defined by that layer type. For example, text rotates around its anchor, while circular graphics use their center. If rotation appears to orbit around an unexpected point, inspect the element's X/Y, center, or origin controls.

For lines and paths, changing endpoints can be more appropriate than rotating the complete layer. For arc text, start angle and direction also affect placement independently of rotation.

## Move several layers together

Hold Shift while selecting multiple layers. The combined selection can be moved as a coordinated set when the active canvas operation supports it.

Create a group when the same collection will be moved repeatedly. Grouping a value, unit label, background, and frame reduces the risk of leaving one part behind.

Use Escape to cancel the current canvas operation or clear a selection that should not be transformed.

## Unlock a layer that will not move

A locked layer remains visible but resists direct canvas manipulation. Select its lock control in the layer list, or press L while it is selected.

Lock a finished background or frame again after positioning it. This prevents it from being dragged while smaller elements above it are edited.

## Keep elements inside the canvas

After a move, scale, or rotation:

- Check every edge at normal preview zoom.
- Confirm that no important stroke or label is clipped.
- Inspect both the shortest and longest telemetry text values.
- Play the timeline to check moving graphics.
- Use "Save Frame" if a clean still is useful for inspecting the layout.

An element can remain selectable while part of it lies outside the exported canvas. Only the canvas area is included in the rendered overlay.

## Save the transformed layout

Use "Save" for an existing custom template or "Save As New" for a new version. Wait for the unsaved indicator to clear before closing the tab or resetting Studio.

The finished layout now uses direct movement for broad composition and exact position, size, and rotation controls for repeatable placement.
