# How to Add a Heading or Compass Overlay to GoPro Video

Shred Scopes can display the GoPro's GPS course as a compass pointer, direction label, or degree value. GPS course describes the direction of travel over the ground; it does not describe the direction the camera lens is pointing.

This distinction is important when the camera turns independently, looks sideways, or remains mounted at an angle to the direction of travel.

## Before starting

Use an original GoPro video containing valid GPS position and course data, or a saved extraction from that video.

Course is most meaningful while the camera is moving. At a stop or very low speed, small GPS position changes can make direction less stable.

## 1. Load a source with GPS course

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio."

Load an original local clip or choose saved telemetry from the account. Wait for preparation to finish and confirm that "GPS course" is available.

If the source has motion data but no usable GPS positions, a travel-direction compass cannot be produced from that source.

## 2. Choose a heading template

Select a heading design at "Choose Template." Built-in options are available in collections such as:

- Black Diamond Heading
- Flagship Heading
- Swell Heading
- Trailhead Heading

These templates are unit agnostic because course uses degrees rather than imperial or metric distance units.

Depending on the templates available to the account, "GPS: Course" may provide another compass-style starting point.

## 3. Confirm the GPS course stream

In the Template Editor, select the data-graphic or data-text layer that displays direction. Confirm that "Stream" is set to "GPS course."

Course uses degrees:

- 0° is north.
- Values increase clockwise.
- 90° is east.
- 180° is south.
- 270° is west.

No unit conversion is required.

Do not label the value as camera bearing or lens direction. The overlay follows travel direction calculated from GPS movement.

## 4. Configure the compass graphic

A course pointer can display a rotating pointer and compass labels. Depending on the selected design, its controls can include:

- Pointer fill, stroke, length, and width
- Full or abbreviated compass labels
- Label size, weight, and radius
- Circle fill, stroke, and dash style
- Graphic origin and placement

Use abbreviated labels such as N, NE, E, and SE for compact overlays. Full labels can be clearer in a large standalone compass.

Keep the graphic's pivot centered and preview a full turn if the source includes one.

## 5. Add numeric or text direction

To show the recorded degree value, use a data-text layer mapped to "GPS course." Add a degree suffix or static degree symbol and select an appropriate number of decimal places.

If the data-text formatting supports compass output, use it to show a direction label instead of raw degrees. Verify label changes around boundaries such as north-to-northeast or east-to-southeast.

Avoid excessive precision. GPS course does not become more accurate merely because more decimal places are displayed.

## 6. Stabilize low-speed behavior

Preview stopped and slow-moving sections. If the pointer jitters while the camera is barely moving, apply moderate smoothing to the course-driven layer.

Smoothing can make the compass easier to read, but excessive smoothing can soften real turns. Inspect quick direction changes after every adjustment.

A visibility condition can hide the compass during unsuitable sections only if a reliable controlling stream and threshold are configured. Test around the threshold so the graphic does not flicker on and off.

## 7. Preview direction of travel

Check:

- A straight section with a known direction
- A left turn
- A right turn
- A reversal or loop
- A stop and restart

Compare the pointer with route progress, not necessarily with where the camera appears to face. A helmet or handheld camera can point away from the path while GPS course remains correct for movement.

## 8. Save and export

Choose "Template" > "Save As New" after modifying a built-in heading design.

For a standalone compass overlay, select an appropriate transparent or keyed export and choose "Export." For a finished video, choose "Composite Mode," place the compass over the source footage, and export the Source Composite file.

Keep the browser tab open and visible until rendering completes.

## If the compass is missing or erratic

Check that:

- The source contains usable GPS course data.
- The layer is mapped to "GPS course."
- The camera was moving during the section being evaluated.
- Smoothing is not so high that actual turns are delayed or concealed.
- The graphic's rotation direction has not been reversed unintentionally.
- The course is being interpreted as direction of travel rather than camera orientation.

The completed overlay now shows the direction of travel as a compass graphic, degree value, or direction label.
