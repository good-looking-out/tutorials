# How to Add and Delete Layers in a Shred Scopes Template

Layers are the individual visual elements inside a Shred Scopes telemetry template. Text, shapes, telemetry graphics, tick marks, images, and nested templates are all added and managed from the Template Editor's "Layers" section.

The position where a layer is added also determines where it begins in the front-to-back draw order.

## Before editing a built-in template

Built-in templates are read-only starting points. If the edited layout should be retained, open the "Template" menu and use "Save As New" to create a custom copy.

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," load a telemetry source, and choose a template. The Template Editor opens when the source and template are ready.

## Add a layer at the front

Use "Add Layer" when the new element should begin at the front of the template:

1. Open "Layers" in the left sidebar.
2. Select "Add Layer."
3. Browse or search the layer picker.
4. Select the required layer type.
5. Review its initial settings when shown.
6. Select "Add Layer" in the picker.

The new layer appears in the layer list and on the canvas. Because it was added at the front, it draws over layers behind it unless its order is changed.

## Add a layer at a specific position

The layer list includes plus controls between top-level layers. Use one of these controls when the intended stack position is already known.

1. Find the two existing layers between which the new element belongs.
2. Select the plus control labeled "Add layer here."
3. Choose the layer type.
4. Select "Add Layer."

The element is inserted at that point in the draw order. This is useful for placing data text above a background but below a foreground frame without rearranging it afterward.

## Choose the appropriate layer type

The picker includes these main choices:

- "shape" for static geometry such as rectangles, circles, lines, grids, and paths
- "text" for fixed wording or unit labels
- "arc·text" for fixed text arranged around an arc
- "data·text" for a telemetry value that changes with the timeline
- "data·graphic" for a telemetry-driven gauge, path, pointer, chart, or other graphic
- "ticks" for a fixed linear or radial scale
- "data·ticks" for a scale whose range can come from telemetry
- "template" for placing another built-in or custom template inside the current one
- "image" for an available image asset

Choose according to behavior, not only appearance. A static text layer cannot become a changing speed value without being replaced by or recreated as data text.

## Select a layer for editing

Select the element on the canvas or select its entry in the layer list. Expand its panel to reach the controls available for that type.

If several elements overlap under the pointer, right-click the canvas and use "Select layer" to identify the intended one. Clear the current selection before editing when there is any uncertainty about which layer is active.

Rename layers as the layout grows. Names such as "Speed value," "Speed unit," "Gauge track," and "Background" are easier to manage than several indistinguishable default names.

## Delete one layer from the layer list

1. Find the layer under "Layers."
2. Select its X control labeled "Delete layer."
3. Review the name in the "Delete Layer" confirmation.
4. Select "Delete Layer."

Review the name carefully when several layers have similar appearances.

## Delete from the canvas

There are two canvas workflows:

- Right-click a selected layer, choose "Delete," and confirm.
- Select one or more layers and press Delete or Backspace to remove the selection immediately.

The keyboard shortcut can remove several selected elements at once and does not use the same confirmation sequence. Clear unintended multi-selection before pressing it.

## Delete a group safely

Deleting a group with "Delete group and layers" removes the group and every layer inside it. It does not merely remove the group container.

If the elements should remain but no longer be grouped, use "Ungroup" instead. The layers return to individual editing without being removed from the template.

## Undo an unintended deletion

Immediately use Command+Z on macOS or Control+Z on Windows and Linux to undo the last deletion. Undo history belongs to the active template tab, so verify that the correct tab is selected first.

If other edits were made after deletion, undo can also reverse those later changes. Check the canvas and layer list after each undo step.

## Review the layout after adding or deleting

After the layer list changes:

- Check the front-to-back order.
- Play the preview if any data-driven element was added.
- Inspect frames with short and long data-text values.
- Confirm that a deleted layer was not supplying a background, mask, label, or unit.
- Check that no empty group remains.

Save the custom template when the layer list and canvas are correct. A separate saved copy preserves the edited layout without altering its built-in starting point.
