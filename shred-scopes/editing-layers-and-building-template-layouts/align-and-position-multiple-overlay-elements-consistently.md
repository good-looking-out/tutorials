# How to Align and Position Multiple Overlay Elements Consistently

The Template Editor can align selected layers to a common edge or center and distribute three or more elements evenly. It also provides centering operations for positioning a layer relative to the canvas or points and rectangles chosen on the canvas.

Use these controls after establishing each element's approximate size and position.

## Open the layout

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and open the template in the Template Editor.

If it is a built-in design, create a custom copy with "Template" > "Save As New."

## Select multiple layers

Select the first layer, then hold Shift while selecting the other elements on the canvas or in the layer list.

The alignment controls appear above the layer list when two or more layers are selected:

- "L," "CX," and "R" align left edges, horizontal centers, or right edges.
- "T," "CY," and "B" align top edges, vertical centers, or bottom edges.

Confirm the selection before aligning. An unintentionally selected background can become the reference geometry and move smaller elements to an unexpected position.

## Align to a common edge

Use left, right, top, or bottom alignment for elements that should form a clean row or column.

Examples include:

- Left-aligning several metric names
- Right-aligning numeric values
- Top-aligning icons in a horizontal status row
- Bottom-aligning several text labels with comparable bounds

Text layers use their visible bounds and anchors, which can differ by font and character shape. After geometric alignment, inspect whether the result also looks optically balanced.

## Align centers

Use "CX" to place selected horizontal centers on the same vertical line. Use "CY" to place vertical centers on the same horizontal line.

Center alignment is useful for:

- Stacking a pointer, hub, and circular gauge
- Centering text over a background shape
- Aligning a value and unit inside a badge
- Building symmetric telemetry layouts

Check the layer origins if an element looks offset after alignment. Text baselines, circle centers, image bounds, and path geometry can produce different visible results.

## Distribute three or more elements

Select at least three unlocked layers, then use:

- "Dist X" to distribute them horizontally
- "Dist Y" to distribute them vertically

Distribution creates consistent spacing along the selected axis. Arrange the elements in their intended general order first, then distribute and inspect the gaps.

Elements with substantially different sizes can have mathematically consistent placement while their visible whitespace appears uneven. Make a small optical correction with keyboard nudges if needed.

## Center one layer on the canvas

Select a layer and right-click the canvas. Available positioning actions include:

- "Center Layer"
- "Center Horizontally"
- "Center Vertically"

Use full centering for a circular gauge or complete title card. Use one-axis centering when the other coordinate is already correct.

## Center relative to chosen geometry

The canvas also provides:

- "Center Horizontally b/w points"
- "Center Vertically b/w points"
- "Center in rect"

Start the operation, then select the requested points or rectangle on the canvas. These actions are useful when an element should be centered within part of the design rather than the complete canvas.

Press Escape to cancel a positioning operation if the wrong reference area was selected.

## Use precise positions and nudges

After alignment, expand each layer and review its X/Y, center, or endpoint values where available.

Use:

- Arrow keys for 1-pixel nudges
- Shift+Arrow keys for 10-pixel nudges

Numeric coordinates make repeated layouts easier to reproduce. Remember that different layer types can use different anchors, so identical X values do not always mean identical visible left edges.

## Group the aligned component

When the aligned elements should remain together:

1. Keep them selected.
2. Choose "Group."
3. Give the group a descriptive name.
4. Move the group as a coordinated component.

Grouping after alignment reduces the risk of disturbing only one element during later layout changes.

## Review at several frames

Data text can change width as telemetry values change. Preview:

- A short value
- A long value
- Negative and positive values
- Values with the highest expected precision

Use appropriate text alignment and fitting controls so a changing number does not make an otherwise aligned layout appear to jump.

## Save the consistent layout

Save the custom template after geometric and optical checks. If experimenting with another arrangement, use "Save As New" to preserve the existing version.

The template now uses shared edges, centers, spacing, and reference geometry to maintain a consistent visual structure.
