# How to Place One Template Inside Another with a Template Layer

A template layer places a complete built-in or custom telemetry template inside another template. This makes it possible to combine reusable gauges, readouts, maps, and decorative components without rebuilding every child layer in the parent design.

Compatible child variables can use a value entered on the nested layer or receive a shared value from a parent template constant.

## Plan the parent and child templates

The parent is the template being edited. The child is the design placed inside it.

Before nesting:

- Choose a child that performs one clear function.
- Confirm that its required telemetry streams are available.
- Save custom child changes.
- Note any color, font, number, or text constants the child exposes.
- Make the parent canvas large enough for the combined layout.

A template layer preserves the child's internal design while allowing the parent to position and scale the complete result.

## Open the parent template

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and open the intended parent in the Template Editor.

Create a custom copy with "Template" > "Save As New" if the parent begins as a built-in design.

## Add the template layer

1. Open "Layers."
2. Select "Add Layer," or use "Add layer here" at the intended stack position.
3. Choose the "template" layer type.
4. Select the built-in or custom child template.
5. Add it to the parent.
6. Rename the layer according to its role, such as "Speed child" or "Route child."

The nested design appears as one layer in the parent's list. Its internal layers remain part of the child template rather than becoming separate top-level parent layers.

## Position the nested template

Select the template layer and configure:

- X
- Y
- Scale
- Rotation
- Blend mode

"Scale" enlarges or reduces the complete child uniformly. This differs from opening the child and changing its internal canvas or layer dimensions.

Use the layer's positioning operations or canvas controls to place it precisely. Check that no important part extends outside the parent canvas.

## Override a child variable with a value

Expand "Template Variables" on the template layer. The section lists compatible values exposed by the child.

To customize only this nested instance:

1. Locate the child variable.
2. Set "Mode" to "Value."
3. Enter or choose the new color, font, number, or text value.
4. Preview the nested result.

Other uses of the same child template are not changed by this instance-specific override.

Select "Clear" to remove the override and restore the child's default value.

## Connect a child variable to the parent

Use a parent template constant when several nested children or parent layers should share the same setting.

First create the parent constant:

1. Open "Template Constants" in the parent.
2. Select "Add constant."
3. Enter a display name and review the variable name.
4. Choose "Color," "Font," "Number," or "Text."
5. Set its initial value and create it.

Then connect the child:

1. Return to the nested layer's "Template Variables."
2. Find a child variable of the matching type.
3. Set "Mode" to "From parent."
4. Choose the parent constant under "Parent."

Only compatible constant types are offered. Changing the parent constant updates every nested variable and parent-layer control that remains connected to it.

## Combine several reusable components

A parent template can contain more than one template layer. For example, a combined telemetry panel can place separate speed, route, altitude, and G-force children inside one canvas.

For a consistent design:

- Connect children to shared color and font constants.
- Use numeric or text constants for compatible exposed child variables.
- Align and distribute the nested layers in the parent.
- Lock completed nested layers against accidental movement.
- Keep the front-to-back order clear.

The active source must contain the streams required by every child. A nested speed template can remain unavailable even when an unrelated route template works correctly.

## Edit the child from the parent

Select the nested layer and choose "Edit Template" to enter the child template. Its internal layers and constants become available for direct editing.

Use "Return" or "Return to parent" when the child changes are complete. Confirm that the revised child still fits its parent position and scale.

Save the appropriate custom template before leaving. Child edits and parent placement are separate concerns, so review the save state of both working contexts.

## Avoid common nesting problems

### The child appears empty

Check that the active source contains its required telemetry and that the child's data mappings are available.

### A variable cannot use the parent constant

Confirm that the types match. A color child variable requires a color constant, while a number variable requires a number constant.

### The child is clipped

Reduce its scale, change X/Y, or enlarge the parent canvas. Only content inside the parent canvas is exported.

### A parent change does not reach the child

Confirm that the child variable uses "From parent" and still points to the intended constant. "Value" creates an instance override instead.

### Clearing a variable changes its appearance

"Clear" restores the child's default value; it does not preserve the removed override.

## Preview and save

Play the telemetry timeline and check every child at several frames. Confirm shared colors and fonts, source compatibility, overlap, and canvas bounds.

Save the custom parent after all nested templates are positioned and connected. The finished template now combines reusable child designs while retaining centralized parent-level control over compatible shared values.
