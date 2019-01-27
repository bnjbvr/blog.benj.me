Title: A Tale Of Linux On The Desktop
Date: 2016-01-27 21:00
Author: Benjamin Bouvier
Tags: opensource
Slug: installing-linux

So I've received a new desktop machine at home, on which only
Windows 10 was installed. I've decided to install Linux, for my day-to-day
hacking.  Unfortunately, when I've plugged the Ubuntu (nobody's perfect) USB
drive to my computer, I had the surprise to see a black screen showing up just
after booting, and nothing else. Here are some notes taken during the
installation of Linux on this machine.

![Twitter fame]({static}/images/installing-linux-twitter.png)

## Graphics not working

Graphics don't work, but we can still install Ubuntu in non-graphic mode
with an [alternate install
image](http://www.ubuntu.com/download/alternative-downloads), namely the
network installer. Let's try that.

The machine has a Nvidia graphics card, so the open-source Nouveau graphics
driver is used by default. Suspecting proprietary drivers might solve the
problem, I decide to download them. Then, to my greatest surprise, I find out
network isn't working, be it the wireless network or Ye Olde Ethernet network.

## Ethernet not working

The computer vendor's website says the network card is an Atheros Killer 2400.
Looking that up on the web with my favorite [search
engine](https://duckduckgo.com), this [StackOverflow
page](http://askubuntu.com/questions/670347/is-there-any-way-to-install-atheros-e2400-drivers)
showed up. The solution to make ethernet work at the end of the installation is
the following:

    modprobe alx
    echo 1969 e0a1 > /sys/bus/pci/drivers/alx/new_id

This enables the module `alx` and registers the device to the module. Now
ethernet is working. Fiuu. Let's keep moving.

## Install All The Drivers!

The [ubuntu's nvidia troubleshooting
page](https://help.ubuntu.com/community/BinaryDriverHowto/Nvidia) gives you a
nice tool that show you what drivers are adapted to your hardware:
`ubuntu-drivers`. Here's an output example given by this command:

    $ sudo ubuntu-drivers devices
    == /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0 ==
    vendor   : NVIDIA Corporation
    modalias : pci:v000010DEd00000FE9sv0000106Bsd00000130bc03sc00i00
    driver   : xserver-xorg-video-nouveau - distro free builtin
    driver   : nvidia-340-updates - distro non-free
    driver   : nvidia-340 - distro non-free
    driver   : nvidia-352 - distro non-free recommended
    driver   : nvidia-352-updates - distro non-free

So this tells me what the recommanded driver for my nvidia card is. For bonus
credit, it also shows me a recommended driver for the builtin WiFi card. Once
I've installed it, it has been working like a charm!

## Moar graphics settings

After the nvidia driver has been installed, a
[tweak](https://help.ubuntu.com/community/BinaryDriverHowto/Nvidia#Screen_Blanks.2FMonitor_Turns_Off)
was needed to ensure the driver outputs video on the DVI port instead of the
VGA port. Beforehand, the `xorg.conf` file was generated thanks to the
`nvidia-xsettings` command.

## Final boss: UEFI

Now that all minimal drivers are correctly installed and configured, let's try
to reboot. Although I've installed the grub bootloader on the main disk, I
can't find a way to access it, even by trying all the lines in the boot menu.

The reason is that I've boot up the USB drive in legacy mode, which is not UEFI
mode. As a matter of fact, Ubuntu has been installed in legacy mode but the
machine is booting with UEFI, so Linux can't be seen from the bootloader.

Fortunately, this is Linux, and everything that has been done can be undone. If
you can find a way to boot with UEFI **and** log in under Linux (maybe
[chrooting](https://help.ubuntu.com/community/BasicChroot)), then you can
follow [this
procedure](https://help.ubuntu.com/community/UEFI#Converting_Ubuntu_into_UEFI_mode).

I couldn't boot in UEFI mode, but I could run the
[Boot-Repair-Disk](http://sourceforge.net/p/boot-repair-cd/home/Home/) on USB
as UEFI, so I've followed the procedure there and converted my installation
into UEFI mode.

## Linux After All

And here we are, with Linux working out of the box^W^W^W^W. So yes, 2016 will
be another year of Linux on the desktop for me; but it still feels unlikely for
a newcomer to install Ubuntu and see it Just Work on any given machine, so
maybe 2017 will be the year of Linux on the desktop, but not 2016.

Many thanks to [@etnbrd](https://twitter.com/etnbrd),
[@martiusweb](https://twitter.com/martiusweb/) and
[@padenot](https://twitter.com/padenot) for the detailed explanations about
some Linux specifics and for advices.

