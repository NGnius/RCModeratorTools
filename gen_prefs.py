import argparse

print("Parsing arguments...")
parser = argparse.ArgumentParser(description='Generates a "prefs" file that Robocraft uses to determine settings')

parser.add_argument('--resolutionx', '--rx', dest='resX', type=int, metavar='x',
                    help='resolution width, in pixels (default:1920)', default=1920) # captures resolution width

parser.add_argument('--resolutiony', '--ry', dest='resY', type=int, metavar='y',
                    help='resolution height, in pixels (default:1080)', default=1080) # captures resolution height

parser.add_argument('--fullscreen', '--fs', dest='is_full', type=int, metavar='n', choices=[0,1],
                    help='Fullscreen not fullscreen (windowed) mode (default:1)', default=1) # captures fullscreen mode

parser.add_argument('--music', '--musicvolume', dest='music', type=float, metavar='float',
                    help='music volume, out of 1 (default:0)', default=0) # captures music volume

parser.add_argument('--fx', '--sound', '--soundvolume', dest='sound', type=float, metavar='float',
                    help='sounds volume, out of 1 (default:0)', default=0) # captures sound volume

parser.add_argument('--speech', '--speechvolume', dest='speech', type=float, metavar='float',
                    help='voice over volume, out of 1 (default:1)', default=1) # captures speech volume

parser.add_argument('--remember', '--rememberme', dest='remember', type=int, metavar='n', choices=[0,1],
                    help='Whether username and password are remembered (default:1)', default=1) # captures state of remember me check on login

parser.add_argument('--gfx', '--graphics', '-q', '--quality', dest='quality', type=int, choices=range(0,6), metavar='int',
                    help='Graphics quality, from 0 to 5 (default:0). 0 is Fastest, 1 is Fast, ..., 5 is Fantastic.', default=0) # captures graphics quality

parser.add_argument('--fps', '--cap', dest='fps', type=int, metavar='int',
                    help='FPS framerate limit (default:60). Will probably default to 60, 120 or 240', default=60) # captures fps cap

parser.add_argument('--capped', '--fpscapped', dest='fps_is_capped', type=int, metavar='n', choices=[0,1],
                    help='FPS limit activated (default:1)', default=1) # captures fps cap checkmark state

parser.add_argument('--camera', '--camerashake', dest='camera_shake', type=int, metavar='n', choices=[0,1],
                    help='FPS limit activated (default:1)', default=1) # captures camera shake checkmark state

args = parser.parse_args()
print("Generating prefs file...")

# generate file contents
content ='''<unity_prefs version_major="1" version_minor="1">'''

# unnecessary stuff at the start of the file (is not added to contents)
'''<pref name="AccessedMenuTAB" type="int">1</pref>
<pref name="DDSDK_EVENT_IN_FILE" type="string">Qg==</pref>
<pref name="DDSDK_EVENT_OUT_FILE" type="string">QQ==</pref>
<pref name="DDSDK_USER_ID" type="string"></pref>
<pref name="Language" type="string">RW5nbGlzaA==</pref>''' # language strings are hard
# TODO: add language support

content+='''
    <pref name="Screenmanager Is Fullscreen mode" type="int">%s</pref>''' % args.is_full
content+='''
    <pref name="Screenmanager Resolution Height" type="int">%s</pref>''' % args.resY
content+='''
    <pref name="Screenmanager Resolution Width" type="int">%s</pref>''' % args.resX
content+='''
    <pref name="screen_resolution_height" type="int">%s</pref>''' % args.resY
content+='''
    <pref name="screen_resolution_width" type="int">%s</pref>''' % args.resX
content+='''
    <pref name="UnityGraphicsQuality" type="int">%s</pref>''' % args.quality
# more unnecessary stuff, usually in the middle of the file
"""content+='''
    <pref name="UnitySelectMonitor" type="int">0</pref>'''
content+='''
    <pref name="afkWarningShown" type="int">0</pref>'''"""
content+='''
    <pref name="rememberme" type="int">%s</pref>''' % args.remember
content+='''
    <pref name="screen_is_full" type="int">%s</pref>''' % args.is_full
content+='''
    <pref name="AFXVolume" type="float">%s</pref>''' % args.sound
content+='''
    <pref name="MusicVolume" type="float">%s</pref>''' % args.music
content+='''
    <pref name="CappedFrameRate" type="int">%s</pref>''' % args.fps
content+='''
    <pref name="CappedFrameRateEnabled" type="int">%s</pref>''' % args.fps_is_capped
content+='''
    <pref name="VoiceOverVolume" type="float">%s</pref>''' % args.speech
content+='''
    <pref name="EnableCameraShake" type="int">%s</pref>''' % args.camera_shake

'''<pref name="unity.player_session_background_time" type="string">MTUzNDEyNTcyMjY0NQ==</pref>
<pref name="unity.player_session_elapsed_time" type="string">MTI3MDcy</pref>
<pref name="unity.player_sessionid" type="string">NjA4NTMzODc2MjA5MjcwNTYyOA==</pref>
<pref name="password" type="string"></pref>
<pref name="username" type="string"></pref>''' # even more unnecessary stuff, usually at the end
content+='''
</unity_prefs>'''

print("Writing to prefs file...")
with open('./prefs', 'w') as file: # always writes to prefs file in local directory
    file.write(content)
# TODO: Add saving filepath optional argument
