# How to Add and Edit Shape Layers in a Telemetry Template

Shape layers provide the static geometry used to structure and decorate telemetry templates. They can create backgrounds, frames, dividers, guide lines, badges, grids, repeated patterns, and custom paths without changing with the telemetry timeline.

Each shape type has its own geometry controls and shares common fill, stroke, dash, blend, and shadow options.

## Open a template for shape editing

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and open a template in the Template Editor.

Use "Template" > "Save As New" before changing a built-in design.

## Add a shape layer

1. Open "Layers."
2. Select "Add Layer," or choose a plus control labeled "Add layer here" at the required stack position.
3. Select "shape."
4. Choose the required shape type.
5. Select "Add Layer."
6. Rename the new layer according to its purpose.

Add a background near the back of the layer stack. Add a foreground frame, marker, or divider at the depth where it should overlap the other elements.

## Choose a shape by purpose

Available geometry includes:

- Rectangle, split rectangle, trapezoid, circle, ellipse, and N-gon
- Line, arc, polyline, SVG path, and dimension line
- Speech bubble and torn label
- Concentric rings, radial rays, radial dots, and starburst
- Grid, squiggle, and barcode-like patterns

Common uses include:

| Purpose | Suitable starting shapes |
| --- | --- |
| Background panel | Rectangle, split rectangle, trapezoid |
| Circular gauge frame | Circle, arc, concentric rings, radial dots |
| Divider or pointer | Line, dimension line, arc |
| Custom outline | Polyline or SVG path |
| Technical backdrop | Grid, barcode, concentric rings |
| Decorative label background | Speech bubble or torn label |

Use the simplest shape that produces the required result. Simple geometry is usually easier to resize and align consistently.

## Edit position and size

Select the shape on the canvas or in the layer list. Its geometry panel changes according to type.

Examples include:

- X, Y, width, and height for rectangles and grids
- Center X/Y or cx/cy and radius for circles and radial patterns
- Separate horizontal and vertical radii for ellipses
- Endpoints for lines, dimension lines, and squiggles
- Start and end angles for arcs
- Inner and outer radii plus counts for repeated radial shapes

Drag supported canvas handles for visual placement, then use the numeric controls for exact geometry. Arrow keys nudge the selected shape by 1 pixel; Shift+Arrow moves it by 10 pixels.

## Create a custom polyline

A polyline is a custom multi-point path drawn directly on the canvas.

1. Add a polyline shape.
2. Select "Draw Shape in Canvas."
3. Place the required points in sequence.
4. Use the finish action when the path is complete.
5. Adjust its stroke and placement.

Plan the point order before drawing. Undo and redraw if the path contains unnecessary crossings or a misplaced point.

## Use an SVG path

The "Path (SVG)" shape draws geometry from path-data instructions entered in "Path data (SVG d)."

Use it when an existing compatible SVG path is available and ordinary shapes cannot reproduce the outline. Confirm that the path fits the canvas and apply fill only when the path is closed and intended to have an interior.

Do not paste an entire SVG document into the path field; it expects the path instructions used to describe the shape.

## Set fill and stroke

Closed shapes can use a fill, while outlines and open shapes use a stroke.

Configure:

- Solid or gradient fill where supported
- Stroke color and width
- Inside, outside, or centered stroke alignment
- Line caps for open ends
- Line joins for corners
- Solid, dashed, or dotted stroke style
- Dash length and gap

An open line or arc may not display a fill. Use stroke controls for those shapes.

When a shape sits behind text, lower its opacity or choose a muted color so it supports readability rather than competing with the telemetry value.

## Add shadow or glow

Enable "Shadow / glow" when the shape needs separation from the background. Adjust:

- Shadow color
- Opacity
- Blur
- Distance
- Angle

A glow normally uses little or no offset with a larger blur. A directional shadow uses distance and angle. Preview the result over representative light and dark source frames.

## Change overlap and blend behavior

Move the shape in the layer list to control whether it appears behind or in front of text and graphics.

Blend mode changes how the complete layer combines with those behind it. Confirm ordinary stacking first, then experiment with blend mode. A blend result can change substantially when the overlay is later placed over different footage.

Lock a finished background or large frame to prevent accidental canvas movement.

## Build a reusable structure

For a badge containing a value and unit:

1. Add a background shape.
2. Add static text for the unit or label.
3. Add data text for the telemetry value.
4. Align the layers.
5. Put the value and label in front of the background.
6. Group the component.

Duplicate the group to create related readouts with consistent geometry.

## Review and save

Check that:

- Shapes remain inside the canvas.
- Strokes are not clipped at the edges.
- Backgrounds do not cover data layers.
- Repeated patterns remain legible at the export size.
- Rounded corners, dash spacing, and shadows scale appropriately.
- Locked state is intentional.

Save the custom template after the geometry and draw order are correct. The shapes now provide a stable visual structure for the animated telemetry layers.
