import PySimpleGUIQt as p
from images import Images
from utilities import downloadFutureRestore, getRealPath, getTypeFutureRestore, DOWNLOAD_DIRECTORY
import webbrowser
import os

def futureRestoreQuestion():
    p.SetOptions(background_color='white', button_color=('white', '#4286f4'))
    layout = [
        [p.Text('I noticed this is your first time running EGTR!', font=('Arial', 12, 'bold'), justification='center')],
        [p.Text('You have to download FutureRestore first. Press Continue to do so.', font=('Arial', 10, 'italic'), justification='center')],
        [p.Button('Cancel'), p.Button('Continue')]
    ]

    window = p.Window('EGTR', no_titlebar=True, keep_on_top=True, grab_anywhere=True).Layout(layout)
    while True:
        event, values = window.Read()
        if event == 'Cancel':
            window.Close()
            exit()
        elif event == 'Continue':
            downloadFutureRestore()
            window.Close()
            exit()

def mainScreen():
    p.SetOptions(background_color='white', button_color=('white', '#4286f4'))
    layout = [
        [p.Image(data_base64=Images.logo, background_color='white', size=(450, 100), click_submits=True, key='_IMAGE_')],
        [p.T('Required:', font=('Arial', 13, 'bold'), justification='center')],
        [p.T('▬' * 35, justification='center')],
        [p.T('Choose IPSW Filepath: ', font=('Arial', 10, 'italic'), justification='left')],
        [p.Input('', key='_IPSW_'), p.FileBrowse(button_color=('white', '#4286f4'))],
        [p.T('Choose Blobs Filepath: ', font=('Arial', 10, 'italic'), justification='left')],
        [p.Input('', key='_BLOBS_'), p.FilesBrowse(button_color=('white', '#4286f4'))],
        [p.T('Choose SEP Filepath: ', font=('Arial', 10, 'italic'), justification='left')],
        [p.Input('', key='_SEP_'), p.FileBrowse(button_color=('white', '#4286f4'))],
        [p.Checkbox('Use Latest SEP \n(Do Not Set SEP Filepath If Using This!)', key='_LATESTSEP_')],
        [p.T('Choose Baseband Filepath: ', font=('Arial', 10, 'italic'), justification='left')],
        [p.Input('', key='_BASE_'), p.FileBrowse(button_color=('white', '#4286f4'))],
        [p.Checkbox('Use Latest Baseband \n(Do Not Set Baseband Filepath If Using This!)', key="_LATESTBASE_")],
        [p.T('Optional: ', font=('Arial', 13, 'bold'), justification='center')],
        [p.T('▬' * 35, justification='center')],
        [p.T('SEP Manifest: ', font=('Arial', 10, 'italic'), justification='left')],
        [p.Input('', key='_SEPMANI_'), p.FileBrowse(button_color=('white', '#4286f4'))],
        [p.T('Baseband Build Manifest: ', font=('Arial', 10, 'italic'), justification='left')],
        [p.Input('', key='_BASEMANI_'), p.FileBrowse(button_color=('white', '#4286f4'))],
        [p.T('Optional Flags:', justification='center', font=('Arial', 13, 'bold'))],
        [p.T('▬' * 35, justification='center')],
        [p.Checkbox('Debug', key='_DEBUG_'), p.Checkbox('No Baseband', key='_NOBASEBAND_')],
        [p.Checkbox('Update', key='_UPDATE_'), p.Checkbox('Wait', key="_WAIT_")],
        [p.T('▬' * 35, justification='center')],
        [p.Button('Exit Recovery', size=(23, 1)), p.Button('Start', size=(23, 1))],
        [p.Button('Exit', size=(23, 1)), p.Button('Donate', size=(23, 1))],
        [p.Button('Open TSSSaver', size=(23, 1)), p.Button('Open ipsw.me', size=(23, 1))],
        [p.T('\nVersion: 1.0.5 | Licensed Under GNU GPLv3 | Click Here For GitHub', click_submits=True, key='_FOOTER_', font=('Arial', 8, 'italic'), justification='center')]
    ]
    
    window = p.Window('EGTR', no_titlebar=True, keep_on_top=True, grab_anywhere=True).Layout(layout)
    while True:
        event, values = window.Read()
        if event == 'Exit':
            window.Close()
            break
        elif event == 'Donate':
            webbrowser.open_new_tab('https://paypal.me/m4csdev')
        elif event == 'Open TSSSaver':
            webbrowser.open_new_tab('https://tsssaver.1conan.com/')
        elif event == 'Open ipsw.me':
            webbrowser.open_new_tab('https://ipsw.me')
        elif event == '_FOOTER_':
            webbrowser.open_new_tab('https://github.com/M4cs/EGTR-Futurerestore')
        elif event == 'Start':
            if values['_LATESTSEP_'] == True:
                latestsep = ' --latest-sep'
                sep_path = ''
            elif values['_LATESTSEP_'] == False:
                latestsep = ''
            if values['_LATESTBASE_'] == True:
                latestbase = ' --latest-baseband'
                base_path = ''
            elif values['_LATESTBASE_'] == False:
                latestbase = ''
            if values['_IPSW_'] == '':
                p.Window('Error', auto_close=True, auto_close_duration=3, keep_on_top=True, no_titlebar=True, grab_anywhere=True).Layout(
                    [[p.T('Error: You must enter an IPSW! ')]]
                ).Read()
            elif values['_IPSW_'] != '':
                ipsw_path = " " + getRealPath(values['_IPSW_'])
            if values['_SEP_'] == '':
                if values['_LATESTSEP_'] == True:
                    latestsep =  '--latest-sep'
                    sep_path = ''
                elif values['_LATESTSEP_'] == False:
                    p.Window('Error', auto_close=True, auto_close_duration=3, keep_on_top=True, no_titlebar=True, grab_anywhere=True).Layout(
                    [[p.T('Error: You must enter an SEP path or choose Use Latest! ')]]
                ).Read()
            elif values['_SEP_'] != '':
                if values['_LATESTSEP_'] == True:
                    sep_path = ''
                    latestsep = ' --latest-sep'
                elif values['_LATESTSEP_'] == False:
                    sep_path = ' -s ' + getRealPath(values['_SEP_'])
                    latestsep = ''
            if values['_BASE_'] == '':
                if values['_LATESTBASE_'] == True:
                    base_path = ''
                    latestbase = ' --latest-base'
                elif values['_LATESTBASE_'] == False:
                    p.Window('Error', auto_close=True, auto_close_duration=3, keep_on_top=True, no_titlebar=True, grab_anywhere=True).Layout(
                        [[p.T('Error: You must enter an Base path or choose Use Latest! ')]]
                    ).Read()
            elif values['_BASE_'] != '':
                if values['_LATESTBASE_'] == True:
                    base_path = ''
                    latestbase = ' --latest-base'
                elif values['_LATESTBASE_'] == False:
                    base_path = ' -b ' + getRealPath(values['_BASE_'])
                    latestbase = ''
            if values['_BLOBS_'] == '':
                p.Window('Error', auto_close=True, auto_close_duration=3, keep_on_top=True, no_titlebar=True, grab_anywhere=True).Layout(
                        [[p.T('Error: You must choose SHSH2 Blobs! ')]]
                    ).Read()
            elif values['_BLOBS_'] != '':
                blobs_path = ' -t' + getRealPath(values['_BLOBS_'])
            if values['_DEBUG_'] == True:
                debug = ' -d'
            elif values['_DEBUG_'] == False:
                debug = ''
            if values['_BASEMANI_'] == '':
                basemani = ''
            elif values['_BASEMANI_'] != '':
                basemani = ' -p' + values['_BASEMANI_']
            if values['_SEPMANI_'] == '':
                sepmani = ''
            elif values['_SEPMANI_'] != '':
                sepmani = ' -m ' + values['_SEPMANI_']
            if values['_NOBASEBAND_'] == True:
                nobaseband = ' --no-baseband'
                base_path = ''
                basemani = ''
            elif values['_NOBASEBAND_'] == False:
                nobaseband = ''
            if values['_UPDATE_'] == True:
                update = ' -u'
            elif values['_UPDATE_'] == False:
                update = ''
            if values['_WAIT_'] == True:
                wait = ' -w'
            elif values['_WAIT_'] == False:
                wait = ''
            if getTypeFutureRestore() == 1:
                futurerestore = getRealPath(DOWNLOAD_DIRECTORY + '/futurerestore')
            elif getTypeFutureRestore() == 2:
                futurerestore = getRealPath(DOWNLOAD_DIRECTORY + '/futurerestore.exe')
            query = futurerestore + blobs_path + base_path + sep_path + latestbase + latestsep + debug + basemani + sepmani + update + nobaseband + wait + ipsw_path
            print(query)
            outputscreen = p.Window('Logs:', no_titlebar=True, keep_on_top=True, grab_anywhere=True).Layout(
                [[p.T('Are You Sure? You may risk bootlooping or bricking your device! ')],
                [p.Button('Cancel'), p.Button('Continue')]])
            while True:
                event, values = outputscreen.Read()
                if event == 'Continue':
                    p.Window('Logs:', no_titlebar=True, keep_on_top=True, grab_anywhere=True, auto_close=True, auto_close_duration=5).Layout(
                [[p.T('Refer To The Terminal For Output ')]]).Read()
                    outputscreen.Close()
                    os.system(query)
                    break
                elif event == 'Cancel':
                    outputscreen.Close()
                    break
    window.Close()
        
