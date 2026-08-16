# How to Pass Template Constants into a Nested Template

A template layer places one complete Shred Scopes template inside another. When the child template exposes compatible variables, the parent can pass its own template constants into that nested instance. This allows several gauges or panels to share colors, fonts, numbers, or text while retaining their separate internal layouts.

The outer design is the parent template. The design placed in a template layer is the child template.

## Prepare the child and parent

Before connecting values:

- Save the intended child template.
- Confirm which color, font, number, or text variables the child exposes.
- Open or create the parent template.
- Add the child through a "template" layer.
- Confirm that the active telemetry source supports the child's data mappings.

If a built-in design is being modified, use "Template" > "Save As New" to create a custom copy.

## 1. Create the parent constant

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and open the parent in the Template Editor.

Then:

1. Open "Template Constants."
2. Select "Add constant."
3. Enter a descriptive display name.
4. Review the variable name.
5. Choose "Color," "Font," "Number," or "Text."
6. Set the initial value.
7. Select "Create."

Create only the constants the parent must control. Examples include `Accent Color`, `Readout Font`, `Gauge Maximum`, and `Unit Label`.

## 2. Select the nested template layer

Select the child instance in "Layers" or on the canvas. Confirm that the selected layer type is "template," then expand "Template Variables."

This section lists compatible variables made available by the child. A child without exposed variables can still be positioned and scaled as a template layer, but it cannot receive a parent value through this section.

## 3. Connect a child variable from the parent

For the intended child variable:

1. Set "Mode" to "From parent."
2. Open "Parent."
3. Choose a parent constant of the matching type.
4. Preview the nested result.

Only compatible types are offered. Connect color to color, font to font, number to number, and text to text.

If the intended constant is missing, confirm that it was created in the current parent template and that its type matches the child variable.

## 4. Choose between From parent, Value, and Clear

Each mode serves a different purpose:

- "From parent" keeps the child variable connected to a parent constant. Updating the parent updates the nested instance.
- "Value" assigns a literal value to this specific nested instance. It no longer follows the parent constant for that variable.
- "Clear" removes the override and restores the child's default value.

Use "From parent" for coordinated design values. Use "Value" for a deliberate exception, such as one warning gauge with a different accent. Use "Clear" when the child should return to its own saved default.

## 5. Connect colors and fonts

A parent color constant can coordinate compatible child fills, strokes, backgrounds, or other exposed paint choices. A parent font constant can coordinate compatible text and tick-label families.

After changing either one, inspect the child at full size. A new color may need a different outline for contrast, and a new font may alter text width or baseline position. The parent supplies the value; it does not automatically refit the child's layout.

## 6. Connect numbers and text

Number and text constants are useful for child variables such as a gauge bound, shared unit, title, threshold, or other exposed customization value.

After connecting a number, verify the gauge, ticks, and data mapping at the minimum and maximum telemetry values. After connecting text, confirm that the longest expected string fits the child canvas.

A parent constant can be connected only when the child exposes a compatible variable. It cannot be applied automatically to an arbitrary number or text field inside the child.

## 7. Coordinate several nested children

Repeat the connection for other template layers in the same parent. For example:

1. Add separate speed, altitude, and G-force child templates.
2. Connect each exposed accent variable to one parent color constant.
3. Connect each exposed font variable to one parent font constant.
4. Connect unit or limit variables where their types and meanings agree.
5. Position and scale the children into the combined layout.

Editing one parent constant should now update every nested variable that remains connected.

Do not connect values merely because their types match. Two numeric variables can have different meanings or units even though both accept numbers.

## 8. Test an instance-specific override

Select one child variable, change "Mode" from "From parent" to "Value," and enter an alternate value. Confirm that only that nested instance changes.

Return it to "From parent" and reselect the constant when it should rejoin the coordinated design. Clearing the override restores the child default, which may differ from the current parent value.

## 9. Edit the child when a variable is absent

If an internal child value must become reusable but is not exposed, select the template layer and use "Edit Template" to open the child. Add or adjust the appropriate child constant and connect compatible internal controls, then save the child and return to the parent.

Review "Template Variables" again after the child is saved. Keep child edits focused: changing the child's internal canvas or layout can affect every parent that uses it.

## 10. Troubleshoot the connection

### The parent constant is not listed

Check the parent constant's type and confirm that the current parent owns it.

### The nested graphic does not change

Confirm that the child variable uses "From parent," points to the intended constant, and has not been changed to "Value."

### The child changes but no longer fits

Open the child and correct its font fitting, label space, gauge bounds, or internal layout. Then return to the parent and recheck its scale and position.

### Another child displays an incorrect unit or limit

Verify meaning and conversion, not only data type. A shared number must represent the same unit and purpose in each child.

## 11. Preview and save both levels

Change each parent constant and inspect every connected child over several telemetry frames. Check minimums, maximums, long text, bright footage, and dark footage.

Save child changes in the child editing context, then save the parent after its connections, placement, and instance overrides are complete. Reopen the parent and confirm that all nested values still follow the intended constants.
