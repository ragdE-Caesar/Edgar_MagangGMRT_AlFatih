# PR 2: Konversi Quaternion ke Roll, Pitch, dan Yaw

Paket `py_pubsub` menerbitkan pesan `geometry_msgs/msg/Quaternion` dengan nilai
yang ditentukan langsung di kode, pada topik `hidup_jokowi`. Subscriber menerima
pesan dari topik dan tipe yang sama, mengonversi quaternion menjadi roll, pitch,
dan yaw, lalu mencetak sudut dalam derajat beserta perkiraan respons robot.

Jalankan kedua node dari workspace ROS 2 yang sudah dimuat:

```bash
ros2 run py_pubsub stalker
ros2 run py_pubsub penguntit
```

Publisher mengirim `(x, y, z, w) = (0, 0, 0.5, 1)`. Semua komponennya berada
dalam rentang `[-1, 1]`. Quaternion ini belum ternormalisasi, sehingga SciPy
menormalisasikannya sebelum konversi. Subscriber menggunakan urutan komponen
`(x, y, z, w)` dan `as_euler('xyz', degrees=True)`. Untuk quaternion yang sudah
ternormalisasi, rumus roll, pitch, dan yaw yang setara adalah:

```text
roll  = atan2(2(wx + yz), 1 - 2(x^2 + y^2))
pitch = asin(clamp(2(wy - zx), -1, 1))
yaw   = atan2(2(wz + xy), 1 - 2(y^2 + z^2))
derajat = radian * 180 / pi
```

Fungsi `clamp` memastikan masukan `asin` tetap berada dalam rentang yang valid
akibat pembulatan bilangan pecahan. Dengan nilai contoh di atas, hasil yang
diharapkan kira-kira `roll=0°`, `pitch=0°`, dan `yaw=53.13°`.

## Asumsi respons robot

Respons ini hanya demonstrasi, bukan pengendali gerak. Asumsinya robot
penggerak diferensial berada di lantai datar, arah maju sejajar sumbu dunia `+X`,
dan yaw nol berarti menghadap ke depan. Jika besar roll atau pitch melebihi
15 derajat, robot berhenti. Jika tidak, yaw di atas 15 derajat berarti berputar
ke kiri, yaw di bawah -15 derajat berarti berputar ke kanan, dan yaw di antara
-15 hingga 15 derajat berarti maju. Yaw positif adalah rotasi berlawanan arah
jarum jam pada sumbu `+Z` (belok kiri).

## Sumber

- [Dokumentasi SciPy: `Rotation.from_quat`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.from_quat.html)
- [Dokumentasi SciPy: `Rotation.as_euler`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.as_euler.html)
- [Dokumentasi ROS 2: `geometry_msgs/msg/Quaternion`](https://docs.ros.org/en/jazzy/p/geometry_msgs/msg/Quaternion.html)
