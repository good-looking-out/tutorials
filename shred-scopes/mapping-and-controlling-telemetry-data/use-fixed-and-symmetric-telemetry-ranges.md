# How to Use Fixed and Symmetric Telemetry Ranges

Telemetry graphics often need either a consistent fixed scale or a scale centered on zero. Shred Scopes provides "fixed range" for explicit input and output limits and "fit max absolute" for a source-dependent symmetric range.

These methods are especially useful for signed acceleration, lateral or longitudinal G, grade, and vertical speed.

## Choose the appropriate method

Use "fixed range" when:

- Several clips must use the same scale.
- A gauge has known minimum and maximum values.
- Zero must remain at a specific visual position.
- The range should not change with the source or selected timeline segment.

Use "fit max absolute" when:

- The stream has positive and negative values.
- Zero should remain centered.
- The range can adapt to the strongest magnitude in the active data.

Use ordinary "fit data min/max" instead only when centering and cross-clip consistency are not required.

## 1. Load the data-driven graphic

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and open the required template.

Select a numeric data-graphic layer and confirm its stream and unit conversion. Create a custom copy with "Template" > "Save As New" when changing a built-in design.

## 2. Configure a fixed range

Open "Map / normalize input" and select "fixed range."

Enter:

- Input minimum
- Input maximum
- Output minimum
- Output maximum

The input values describe the converted telemetry. The output values describe the range expected by the graphic.

For a signed gauge, use equal-magnitude input limits when zero should sit at the midpoint. For an unsigned speedometer, a minimum of zero and a suitable positive maximum is more typical.

## 3. Match fixed ticks and labels

Use static or manual-bound data ticks with the same converted minimum and maximum. Set their direction to match the graphic.

Confirm that:

- The minimum label sits at the graphic's minimum position.
- Zero appears at the intended point.
- The maximum label sits at the maximum position.
- Unit suffixes match the conversion.

A fixed graphic with automatically derived ticks can show a different numeric scale. Keep both on the same range strategy.

## 4. Configure fit max absolute

Select "fit max absolute" when the active data should determine the range but zero must stay centered.

Shred Scopes finds the largest positive or negative magnitude and uses it for equal limits around zero. If the strongest value is negative, its magnitude also determines the positive side; if the strongest value is positive, the negative side receives the same magnitude.

This is useful for:

- Acceleration versus braking
- Climbing versus descending vertical speed
- Left versus right lateral G
- Forward versus backward longitudinal G
- Uphill versus downhill grade

The scale can change when the source or selected range changes.

## 5. Configure symmetric data ticks

For data ticks mapped to the same stream:

1. Choose the same conversion.
2. Set "Bounds source" to the telemetry stream.
3. Enable "Symmetric around zero."
4. Enable "Include zero" if it is not already guaranteed by the symmetric scale.
5. Configure major and minor intervals.

Use "Nice scale" when rounded endpoints and steps are preferable to the exact recorded magnitude.

## 6. Set units before ranges

Unit conversion occurs before fixed mapping. A range entered after conversion to mph represents mph, not m/s. Changing the unit requires reviewing:

- Fixed input limits
- Tick limits and step
- Clamp values
- Deadband values
- Visibility thresholds

Do not reuse an unchanged numeric range after changing units unless the numbers remain intentionally appropriate.

## 7. Decide how out-of-range values behave

A fixed map defines how an input interval maps to output. It does not necessarily mean that values outside the interval are removed.

Use:

- "Clamp values" to limit the incoming converted telemetry before mapping
- "Clamp mapped output" to limit the result produced by the fixed-range map

These controls solve different problems. Input clamping changes the value used by that layer; output clamping keeps the mapped visual result within its intended output span.

## 8. Rebuild and preview

For "fit max absolute," set the final in and out points and use "Rebuild data graphics from range" so the adaptive magnitude represents the selected segment.

Preview:

- Zero or neutral movement
- The strongest positive event
- The strongest negative event
- Several middle values
- Any value beyond a fixed input limit

Check that direction, sign, tick labels, colors, and pointer movement agree.

## 9. Compare clips carefully

A fixed range makes the same value occupy the same visual position across clips. "Fit max absolute" does not: it adapts to each active data set.

Use fixed ranges for comparison videos or a consistent template series. Use an adaptive symmetric range when the priority is making each clip's signed motion visible across the full graphic.

## 10. Save the range configuration

Save the custom template after its graphic, data text, and ticks use compatible units and ranges.

The completed layout now uses either an explicit repeatable scale or a zero-centered adaptive scale suited to signed telemetry.
