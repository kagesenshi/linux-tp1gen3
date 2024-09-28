# Linux support patches for Lenovo X1 Tablet 3rd generation

 - [HID driver patches (keyboard functional keys and LEDs)](#linux-hid-patches)
  - [Installation on Arch Linux](#arch-linux-installation)
  - [Installation on Ubuntu (and possibly other distributions)](#ubuntu-installation-dkms)
 - [Additional Information](#additional-information)


## Removed items (newer kernels handle it correctly)

- ACPI patches
- hid-multitouch patches 

## Linux HID Patches

**Caution**: These steps will modify your kernel. Doing so might prevent your system from booting.

The attachable keyboard uses non standard keycodes for the functional keys and an additional USB endpoint for control of the LEDs. The provided sourcecode is a patched version of the upstream [hid-lenovo module][hid-lenovo]. For reference the patches (for the first generation device?) by [Dennis Wassenberg][hid-lenovo-patches] were used. 

Prerequisites:
 - make
 - GCC C compiler
 - Linux headers/source for the currently installed kernel

### Arch Linux installation
When running Arch Linux you may build the DKMS package and install it via pacman:

```{.sh}
cd hid
makepkg .
pacman -U hid-lenovo-tp1gen3-dkms-0.2.0-1-x86_64.pkg.tar.xz
```

If you install the compiled module keep in mind, that you have to recompile the module every time your kernel is updated.

```{.sh}
cd hid
make
sudo make install
```

As the multitouch module is not an extension but a replacement of the upstream module, the latter must be blacklisted. While the Arch Linux package should add the necessary lines
automatically it might be necessary to regenerate the initramfs as the original module also must be replaced there. For details see [here][aw-blacklisting].

### Fedora installation (DKMS)
1. Enable copr repository
```
dnf copr enable izhar/hid-lenovo-tp1gen3 
```
2. install RPM
```
dnf install hid-lenovo-tp1gen3
```

### Ubuntu installation (DKMS)

1. download and extract `linux-tp1gen3-master` 
```
cd linux-tp1gen3-master
```

2. install the DKMS package
```{.sh}
sudo apt-get install build-essential dkms 
```

3. copy files
```{.sh}
sudo mkdir -p /usr/src/hid-lenovo-tp1gen3-<version>
sudo cp -a ./hid/src/* /usr/src/hid-lenovo-tp1gen3-<version> 
```

4. build and install
```{.sh}
sudo dkms add -m hid-lenovo-tp1gen3 -v <version>
sudo dkms build -m hid-lenovo-tp1gen3 -v <version>
sudo dkms install -m hid-lenovo-tp1gen3 -v <version>
```
Check if the module was successfully added to dkms
```{.sh}
~$ dkms status
hid-lenovo-tp1gen3, 0.2.0, 5.6.14, x86_64: installed
```

5. blacklist the old module
   Add `blacklist hid-multitouch` to the file `/etc/modprobe.d/blacklist.conf`
   Then reboot.

## Contributions
Thanks goes to
 * [bitbacchus](https://github.com/bitbacchus) for writing the Ubuntu Installation section
 * [parenthetical](https://github.com/parenthetical) for providing the BIOS patch for version 1.35


## Additional Information

 * [intel hid module description (aka the volume buttons) ](https://lkml.org/lkml/2018/6/28/636)
 * [Kernel sleep state information](https://www.kernel.org/doc/html/v4.15/admin-guide/pm/sleep-states.html)
 * [Arch Linux Wiki on using the generated apci_override and DSDT in general](https://wiki.archlinux.org/index.php/DSDT#Using_a_CPIO_archive)

[dxi]: https://delta-xi.net/blog/#056 "Delta-Xi Blog"
[hid-lenovo]: https://github.com/torvalds/linux/blob/9f7582d15f82e86b2041ab22327b7d769e061c1f/drivers/hid/hid-lenovo.c "Linux hid-lenovo module sourcecode"
[hid-multitouch]: https://github.com/torvalds/linux/blob/9f7582d15f82e86b2041ab22327b7d769e061c1f/drivers/hid/hid-multitouch.c "Linux hid-multitouch module sourcecode"
[hid-lenovo-patches]: https://www.spinics.net/linux/fedora/linux-sound/msg00626.html "hid-lenovo: Add support for X1 Tablet special keys and LED control"
[aw-blacklisting]: https://wiki.archlinux.org/index.php/Kernel_module#Blacklisting
[poinstick-issue]: https://github.com/Lunm0us/linux-tp1gen3/issues/2

