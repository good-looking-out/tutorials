# How to Change the Front-to-Back Order of Template Layers

Every Shred Scopes template has a draw order. Layers nearer the front of the "Layers" list render over layers behind them, allowing text and telemetry graphics to appear above backgrounds, frames, images, and other elements.

Changing order affects overlap; it does not move a layer to a different X or Y position.

## Open the layer stack

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and open a template in the Template Editor.

Expand "Layers" in the sidebar. The list represents the template's current stacking order.

A common simple stack is:

1. Foreground text or pointer
2. Gauge progress or telemetry graphic
3. Tick marks and labels
4. Decorative frame
5. Background shape

The exact order depends on which parts should overlap.

## Move a layer by dragging it in the list

Drag a layer entry to another insertion position. Watch the placement indicator and release it at the intended point.

After moving the entry, check the canvas. A layer can appear to vanish if it is now behind an opaque background or image.

Dragging is efficient for a large move, such as placing a newly added rectangle behind the entire design.

## Move one step at a time

Use the layer's arrange controls or canvas right-click menu for smaller changes:

- "Send backward" moves the selection one position toward the back.
- "Bring forward" moves it one position toward the front.
- "Send to back" moves it behind the other layers in the current ordering scope.
- "Bring to front" moves it ahead of the other layers in the current ordering scope.

The up and down arrange controls in the layer list provide the same kind of stepwise adjustment where shown.

## Use keyboard shortcuts

With a layer selected:

- Command+[ on macOS or Control+[ on Windows and Linux sends it backward one step.
- Command+] or Control+] brings it forward one step.
- Command+Option+[ or Control+Alt+[ sends it to the back.
- Command+Option+] or Control+Alt+] brings it to the front.

After using a shortcut, inspect the layer list rather than relying only on the current frame. Transparent areas can make order changes difficult to see.

## Add a new layer at the correct depth

Instead of adding every element at the front and rearranging it, use a plus control labeled "Add layer here" between existing top-level layers.

For example, insert a background immediately behind the text and gauge layers but in front of a larger decorative image. The new layer begins at the selected draw position.

## Order layers inside and around groups

Groups organize related layers into one structure. Ordering actions operate within the current scope:

- Reorder child layers inside the group to change how they overlap one another.
- Move the group in the top-level list to change how the complete grouped design overlaps other top-level layers.
- Ungroup when elements need to be distributed into separate stack positions.

Collapsing a group hides its children in the sidebar but does not hide them on the canvas or change their draw order.

## Select a layer hidden by overlap

When an opaque or larger element covers the intended layer:

1. Select its name in the layer list, or right-click the overlap.
2. Use "Select layer" to choose the intended element.
3. Bring it forward or move the covering element backward.

Temporarily use the eye control to hide the covering layer if necessary. Hiding is reversible and does not remove the element.

## Distinguish order from blend mode and opacity

Draw order decides which layer is placed first or later. Opacity changes how much of a layer is visible, and blend mode changes how it combines with layers below it.

If bringing a layer forward does not produce the expected result, check:

- The layer's visibility
- Its whole-layer opacity
- Fill and stroke opacity
- Blend mode
- Whether another opaque layer remains in front

Solve the stack first, then adjust blend behavior.

## Check common stacking problems

Review these cases:

- A background rectangle belongs behind all readable content.
- A frame may belong in front of the background but behind text.
- A gauge pointer normally belongs in front of its track and ticks.
- A progress graphic may need to appear over a muted track.
- A logo or image may need to sit behind telemetry text but above the background.
- An image used for clipping depends on the compatible clipping layer selected for it, not only on ordinary draw order.

Preview the template at several telemetry frames because moving graphics can overlap differently as values change.

## Save the new order

Save the custom template after the layer stack is correct. If experimenting with a substantially different arrangement, use "Save As New" to keep the previous version available.

The template now draws each element at the intended depth while retaining its original canvas position and animation behavior.
