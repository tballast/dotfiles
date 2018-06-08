#!/usr/bin/python3

# -*- coding: utf-8 -*-
from i3pystatus import Status


status = Status()

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
                format="🕑 %a %-d %b %H:%M:%S",
                color="#50C878")

# status.register("shell",
#                 command="python3 ~/.config/i3/msexchangeclient.py mail",
#                 interval=5,
#                 color="#41eef4")

# status.register("shell",
#                 command="python3 ~/.config/i3/msexchangeclient.py up-meeting",
#                 on_leftclick="python3 ~/.config/i3/msexchangeclient.py dismiss-meeting",
#                 on_rightclick="python3 ~/.config/i3/msexchangeclient.py show-meetings",
#                 interval=5,
#                 color="#E5B800")


status.register("uptime",
                format="🕰 {days}:{hours}:{mins}:{secs}",
                color="#FFF0FF")

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
                format=" {volume}%",
                format_muted=" {volume}%")


# # Shows the average load of the last minute and the last 5 minutes
# # (the default value for format is used)
# # status.register("load",
# #     format=" {avg1}",
# #     color="#6c71c4")


# Shows your CPU temperature, if you have a Intel CPU
# status.register("temp",
#                 format="🌡 {temp:.0f}°C",
#                 file="/sys/class/thermal/thermal_zone2/temp",
#                 color="#b58900")

status.register("cpu_usage_graph",
                graph_style="braille-snake",
                start_color="#6c71c4",
                format="{cpu_graph}{usage}%")

status.register("mem_bar",
    multi_colors="true")


# # # The battery monitor has many formatting options, see README for details

# # # This would look like this, when discharging (or charging)
# # # ↓14.22W 56.15% [77.81%] 2h:41m
# # # And like this if full:
# # # =14.22W 100.0% [91.21%]
# # #
# # # This would also display a desktop notification (via D-Bus) if the percentage
# # # goes below 5 percent while discharging. The block will also color RED.
# # # If you don't have a desktop notification demon yet, take a look at dunst:
# # #   http://www.knopwob.org/dunst/
# # status.register("battery",
# #     format="{status}/{consumption:.2f}W {percentage:.2f}% [{percentage_design:.2f}%] {remaining:%E%hh:%Mm}",
# #     alert=True,
# #     alert_percentage=5,
# #     status={
# #         "DIS": "↓",
# #         "CHR": "↑",
# #         "FULL": "=",
# #     },)

# # # This would look like this:
# # # Discharging 6h:51m
# # status.register("battery",
# #     format="{status} {remaining:%E%hh:%Mm}",
# #     alert=True,
# #     alert_percentage=5,
# #     status={
# #         "DIS":  "Discharging",
# #         "CHR":  "Charging",
# #         "FULL": "Bat full",
# #     },)

# # Displays whether a DHCP client is running
# # status.register("runwatch",
# #     name="DHCP",
# #     color_up="#FF0000",
# #     path="/var/run/dhclient*.pid",)

# # Shows the address and up/down state of eth0. If it is up the address is shown in
# # green (the default value of color_up) and the CIDR-address is shown
# # (i.e. 10.10.10.42/24).
# # If it's down just the interface name (eth0) will be displayed in red
# # (defaults of format_down and color_down)
# #
# Note: the network module requires PyPI package netifaces
status.register("network",
                interface="eth0",
                format_up=" {v4cidr}",
                format_down=" {interface}: DOWN")

status.register("network",
                interface="eth0",
                format_up="↑ {bytes_sent}KB/s",
                start_color="#E91E63")

status.register("network",
                interface="eth0",
                hints={"separator": False},
                format_up="↓ {bytes_recv}KB/s",
                start_color="#00BCD4")


# # # Note: requires both netifaces and basiciw (for essid and quality)
# # status.register("network",
# #     interface="wlan0",
# #     format_up="{essid} {quality:03.0f}%",)

# # Shows disk usage of /
# # Format:
# # 42/128G [86G]
# status.register("disk",
#    path="/",
#    format=" {used}/{total}G [{avail}G]",
#    color="#859900")


# status.register("makewatch",
#                 running_color="#00BCD4",
#                 idle_color="#50C878",
#                 interval=1,
#                 format="🔨 🔧")


status.register("uname",
                format=" {release}")

# status.register("weathercom",
#                 location_code="N6N1E4"
#                 )

# status.register("myweather",
#                 color='#e97ac8',
#                 )

# # Shows mpd status
# # Format:
# # Cloud connected ▶ Reroute to Remain
status.register("spotify",
                color='#81b71a',
                format="🎶 {artist} - {title} {status}",
                status={
                    'paused': '⏸',
                    'playing': '▶',
                    "stop": "⏹"
                })

status.run()
