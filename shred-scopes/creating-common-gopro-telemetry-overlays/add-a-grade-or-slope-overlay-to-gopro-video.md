# How to Add a Grade or Slope Overlay to GoPro Video

Shred Scopes can display uphill and downhill grade calculated from GoPro GPS movement. A grade overlay can use numeric text, a slope-angle graphic, a tilt horizon, or another signed indicator.

Grade depends on valid ground-speed and altitude changes. It describes the path's slope rather than the camera's physical tilt.

## Before starting

Prepare an original GoPro recording with usable GPS speed and altitude data, or saved telemetry from that recording.

Grade becomes less reliable when the camera is stationary, moving very slowly, or receiving inconsistent GPS measurements. The Template Editor includes grade-specific smoothing controls to make the display more readable.

## 1. Load the telemetry source

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio."

Choose the original clip or saved telemetry and wait until Studio prepares the source. Confirm that "Grade (slope)" is available before selecting a grade template.

## 2. Choose a grade template

Select a grade or slope design at "Choose Template." Examples are available in collections such as:

- Black Diamond Slope
- Flagship Grade or Flagship Grade Text
- Swell Grade or a Swell Grade Text layout
- Trailhead Grade or Trailhead Grade Text

Depending on the templates available to the account, other layouts can include a slope angle, rise-and-run graphic, terrain profile, or tilt horizon.

The selected design opens in the Template Editor.

## 3. Choose percent or angle

Select the grade-driven data-text or data-graphic layer and confirm that its "Stream" is "Grade (slope)."

Grade uses percent by default:

- Positive values indicate an uphill grade.
- Negative values indicate a downhill grade.
- Zero represents level travel.

Available conversions can display:

- Signed slope angle in degrees, preserving uphill and downhill direction
- Absolute steepness in degrees, removing the sign

Percent grade and angle are not the same scale. Update unit labels and tick values when changing between them.

Use signed values when direction matters. Use absolute steepness only when the display is intended to show how steep the path is without distinguishing climbing from descending.

## 4. Configure grade smoothing

Selecting "Grade (slope)" exposes grade-specific controls:

- "Smoothing" reduces rapid changes in the displayed grade.
- "Adaptive Smoothing" adjusts stabilization based on surrounding motion and GPS reliability.
- "Low Motion Hold" keeps the value nearer a reliable surrounding grade during stopped or nearly stopped sections while adaptive smoothing is enabled.

Start with moderate smoothing and preview both sustained slopes and short transitions. Increasing smoothing can suppress spikes, but very high settings can also soften genuine short climbs or descents.

Use "Low Motion Hold" when the grade readout wanders while the camera is barely moving. Leave it off when small low-speed changes must remain visible.

## 5. Set a signed visual range

A grade gauge should normally show both downhill and uphill values around zero.

Useful mapping choices include:

- "fit max absolute" for a symmetric range based on the largest positive or negative grade
- "fixed range" for a consistent scale, such as an equal downhill and uphill span

A symmetric range places level travel at the visual center and makes opposite slopes comparable. Avoid "fit data min/max" when unequal recorded extremes would shift zero away from the intended neutral position.

If isolated GPS spikes dominate the range, use "Clamp values" with limits appropriate to the activity and selected unit. Clamping should be used to control display behavior, not to imply that the underlying GPS was corrected.

## 6. Preview climbs, descents, and stops

Scrub to:

- A level section
- A sustained climb
- A sustained descent
- A stop or low-speed section
- A sharp transition

Confirm that the sign, graphic direction, numeric text, and labels agree. If an uphill section produces a negative display, check whether the graphic's direction was reversed or whether a layer uses a different mapping.

Avoid interpreting momentary grade spikes at nearly zero ground speed as precise trail slope.

## 7. Save and export

Use "Template" > "Save As New" after customizing a built-in template.

For a separate overlay, select a transparency-capable format or keyed-background MP4 in the Template Editor and choose "Export." Keep the tab open and visible until rendering finishes.

For a finished telemetry video, choose "Composite Mode," place the grade design over the original footage, preview it across changing backgrounds, and export the Source Composite file.

## If grade is missing or unstable

Check that:

- The original clip contains valid GPS speed and altitude data.
- "Grade (slope)" is available and selected.
- The camera was moving sufficiently for a meaningful path slope.
- The percent or degree conversion matches the unit label.
- Smoothing is not so high that real changes disappear.
- A fixed range or clamp is not hiding expected values.

The completed overlay now shows the direction and magnitude of the recorded path's slope with stabilization appropriate to the footage.
