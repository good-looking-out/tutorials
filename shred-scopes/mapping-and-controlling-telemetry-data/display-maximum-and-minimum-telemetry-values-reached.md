# How to Display Maximum and Minimum Telemetry Values Reached

Running maximum and running minimum streams retain the highest or lowest value reached so far as the timeline advances. They can create peak-speed, minimum-altitude, strongest-G, or related readouts that update only when a new extreme occurs.

These are progressive values, not fixed summaries displayed from the first frame.

## Supported running-extreme sources

Running maximum and minimum variants are available when the source contains a supported base stream, including:

- Speed 2D
- Speed 3D
- Altitude
- GPS-path acceleration
- G-force
- Lateral G
- Longitudinal G

The derived variant uses the same default unit and conversion choices as its base stream.

## 1. Load the source and template

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and load the intended GoPro telemetry.

Open a template or create a new custom design. Confirm that the base measurement is available in the active source.

## 2. Add the peak or minimum text

1. Open "Layers."
2. Add a "data·text" layer.
3. Open "Stream."
4. Select the running maximum or running minimum variant of the required base stream.
5. Choose the unit conversion.
6. Configure decimal places, prefix, suffix, and text fitting.
7. Add a static label such as "MAX SPEED" or "MIN ALTITUDE."

Use wording that identifies both the measurement and the type of extreme.

## 3. Understand progressive behavior

A running maximum begins with the starting value and retains the highest value encountered so far. It changes only when a later frame exceeds that value.

A running minimum behaves in the opposite direction. It retains the lowest value encountered so far and changes only when a later frame goes lower.

At the final frame, the running value represents the extreme reached across the complete active data range. At earlier frames, it represents only the portion reached by the playhead.

## 4. Pair the current and extreme values

A useful layout can show:

- Current speed and maximum speed
- Current altitude and minimum altitude
- Current G-force and maximum G-force
- Current acceleration and running maximum or minimum acceleration

Map one data-text layer to the base stream and another to its running variant. Apply the same conversion and compatible numeric formatting.

Use distinct static labels or styling so the current value is not confused with the retained extreme.

## 5. Handle signed streams correctly

For lateral G, longitudinal G, and acceleration:

- Running maximum retains the most positive value reached.
- Running minimum retains the most negative value reached.

The value with the greatest absolute magnitude is not always the running maximum. A strong negative braking event belongs in the running minimum, while a strong positive acceleration belongs in the running maximum.

Display both when positive and negative extremes matter.

## 6. Set units and formatting

Choose the conversion before setting decimals, prefixes, suffixes, or any clamps.

The base and running layers should normally use the same unit. Examples include:

- mph for current and maximum speed
- feet for current and minimum altitude
- ft/s² for acceleration extremes
- g for G-force extremes

Preview the widest formatted value so the retained peak does not overflow the layout.

## 7. Rebuild for a selected range

When the extreme should describe only an exported segment:

1. Set the final in point.
2. Set the final out point.
3. Choose "Rebuild data graphics from range."
4. Return to the first frame and confirm the running value starts from the selected segment.
5. Scrub to the end and review the final extreme.

Without rebuilding, a prior event outside the desired segment can continue to influence range-relative values.

## 8. Treat clamps carefully

Clamping a running-extreme layer can cap what that layer reports. A maximum-speed layer clamped at 60 mph cannot display a higher value even if the source contains one.

If an isolated spike appears to create an implausible peak, review it against nearby frames before clamping. A clamped peak is a limited presentation, not a corrected source record.

Keep base and running layers consistent when they are intended to agree.

## 9. Preview the update sequence

Play through several events and confirm that:

- The running maximum never falls.
- The running minimum never rises.
- A new extreme updates at the correct moment.
- Current values can move away while the extreme remains retained.
- The final value matches the expected active-range extreme.

Check both directions for signed streams.

## 10. Save the extreme-value display

Save the custom template after labels, units, selected range, and signed interpretation are correct.

The overlay now shows the highest or lowest supported GoPro telemetry value reached progressively through the active timeline range.
