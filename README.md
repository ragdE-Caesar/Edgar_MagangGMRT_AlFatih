# PR 2: Quaternion to Roll, Pitch, Yaw

The `py_pubsub` package publishes a hard-coded
`geometry_msgs/msg/Quaternion` on `hidup_jokowi`. The subscriber reads the same
topic and message type, converts the quaternion to roll, pitch, and yaw, and
prints the angles in degrees along with a simple robot response.

Run the nodes from a sourced ROS 2 workspace:

```bash
ros2 run py_pubsub stalker
ros2 run py_pubsub penguntit
```

The publisher sends `(x, y, z, w) = (0, 0, 0.5, 1)`. These components are all
within `[-1, 1]`; the quaternion is not unit length, so SciPy normalizes it
before conversion. The subscriber uses SciPy's scalar-last `(x, y, z, w)`
convention and `as_euler('xyz', degrees=True)`. For a normalized quaternion,
the equivalent roll-pitch-yaw equations are:

```text
roll  = atan2(2(wx + yz), 1 - 2(x^2 + y^2))
pitch = asin(clamp(2(wy - zx), -1, 1))
yaw   = atan2(2(wz + xy), 1 - 2(y^2 + z^2))
degrees = radians * 180 / pi
```

The clamp keeps the pitch input in the valid `asin` range in the presence of
floating-point rounding. With the sample input, the expected result is about
`roll=0°`, `pitch=0°`, `yaw=53.13°`.

## Robot-response assumption

This is only a demonstration, not a motion controller. It assumes a differential
drive robot standing on a flat floor, with its forward direction aligned to
world `+X` and zero yaw. A roll or pitch magnitude above 15 degrees means
`Berhenti`; otherwise yaw above 15 degrees means `Putar ke kiri`, yaw below
-15 degrees means `Putar ke kanan`, and values in the yaw deadband mean
`Jalan maju`. Positive yaw is counter-clockwise about `+Z` (left turn).

## References

- [SciPy `Rotation.from_quat`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.from_quat.html)
- [SciPy `Rotation.as_euler`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.as_euler.html)
- [ROS 2 `geometry_msgs/msg/Quaternion`](https://docs.ros.org/en/jazzy/p/geometry_msgs/msg/Quaternion.html)
