import wx
import sys
import os
import LicentaBackend.haardetection
import LicentaBackend.createBg
import LicentaBackend.annotation
import LicentaBackend.vect


panels = {}
displayed_panel = ''


class MainApplication(wx.App):
    def OnInit(self):
        frame = MainFrame(parent=None, title="Animal recognition toolkit")
        frame.SetMinSize(size=(700, 400))
        frame.Show()
        return True


class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(900, 450))

        menu = MenuPanel(self)
        detection = DetectionPanel(self)
        recognition = RecognitionPanel(self)
        full_detection = FullDetectionPanel(self)
        train_cnn = TrainCNNPanel(self)
        train_haar = TrainHaarClPanel(self)
        output_panel = OutputPanel(self)
        create_samples = CreateSamplesPanel(self)
        crop_panel = CropPanel(self)

        #menu.SetBackgroundColour('blue')
        recognition.SetBackgroundColour('red')

        global panels, displayed_panel
        panels['detection'] = detection
        panels['recognition'] = recognition
        panels['train_haar'] = train_haar
        panels['create_samples'] = create_samples
        panels['output_panel'] = output_panel
        panels['crop_panel'] = crop_panel

        displayed_panel = 'detection'

        frame_box = wx.BoxSizer(wx.VERTICAL)
        frame_box.Add(menu, 1, wx.EXPAND)
        frame_box.Add(detection, 6, wx.EXPAND)
        frame_box.Add(recognition, 6, wx.EXPAND)
        frame_box.Add(full_detection, 6, wx.EXPAND)
        frame_box.Add(train_cnn, 6, wx.EXPAND)
        frame_box.Add(train_haar, 6, wx.EXPAND)
        frame_box.Add(output_panel, 6, wx.EXPAND)
        frame_box.Add(create_samples, 6, wx.EXPAND)
        frame_box.Add(crop_panel, 6, wx.EXPAND)

        recognition.Hide()
        full_detection.Hide()
        train_cnn.Hide()
        train_haar.Hide()
        output_panel.Hide()
        create_samples.Hide()
        crop_panel.Hide()

# self.SetAutoLayout(True)
        self.SetSizer(frame_box)
# self.Layout()


class MenuPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        menu = BoxMenu(wx.HORIZONTAL)
        button1 = wx.Button(self, label='Detection', size=(80, 50))
        button2 = wx.Button(self, label='Recognition', size=(80, 50))
        button3 = wx.Button(self, label='Full Detection', size=(80, 50))
        button4 = wx.Button(self, label='Train CNN', size=(80, 50))
        button5 = wx.Button(self, label='Train Haar Cl', size=(80, 50))
        button6 = wx.Button(self, label='Output', size=(80, 50))
        button7 = wx.Button(self, label='Make Samples', size=(80, 50))
        button8 = wx.Button(self, label='CropImages', size=(80, 50))

        button1.Bind(wx.EVT_BUTTON, self.click1)
        button2.Bind(wx.EVT_BUTTON, self.click2)
        button3.Bind(wx.EVT_BUTTON, self.click3)
        button5.Bind(wx.EVT_BUTTON, self.click5)
        button6.Bind(wx.EVT_BUTTON, self.click6)
        button7.Bind(wx.EVT_BUTTON, self.click7)
        button8.Bind(wx.EVT_BUTTON, self.click8)

        menu.Add(button1, 0)
        menu.Add(button2, 0)
        menu.Add(button3, 0)
        menu.Add(button4, 0)
        menu.Add(button5, 0)
        menu.Add(button6, 0)
        menu.Add(button7, 0)
        menu.Add(button8, 0)
        self.SetSizer(menu)

    def click1(self, event):
        print('a fost apasat butonul 1')
        global displayed_panel
        panels[displayed_panel].Hide()
        panels['detection'].Show()
        displayed_panel = 'detection'

    def click2(self, event):
        print('a fost apasat butonul 2')
        global displayed_panel
        panels[displayed_panel].Hide()
        panels['recognition'].Show()
        panels['recognition'].GetParent().Layout()
        displayed_panel = 'recognition'

    def click3(self, event):
        print('a fost apasat butonul 3')

    def click5(self, event):
        print('a fost apasat butonul 5')

        global displayed_panel
        panels[displayed_panel].Hide()
        panels['train_haar'].Show()
        panels['train_haar'].GetParent().Layout()
        displayed_panel = 'train_haar'

    def click6(self, event):
        print('a fost apasat butonul 6')

        global displayed_panel
        panels[displayed_panel].Hide()
        panels['output_panel'].Show()
        panels['output_panel'].GetParent().Layout()
        displayed_panel = 'output_panel'

    def click7(self, event):
        print('a fost apasat butonul 7')

        global displayed_panel
        panels[displayed_panel].Hide()
        panels['create_samples'].Show()
        panels['create_samples'].GetParent().Layout()
        displayed_panel = 'create_samples'

    def click8(self, event):
        print('a fost apasat butonul 8')

        global displayed_panel
        panels[displayed_panel].Hide()
        panels['crop_panel'].Show()
        panels['crop_panel'].GetParent().Layout()
        displayed_panel = 'crop_panel'


class BoxMenu(wx.BoxSizer):
    def __init__(self, orient):
        super().__init__(orient)


class DetectionPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        mainbox = wx.BoxSizer(wx.VERTICAL)

        data_box = BoxMenu(wx.HORIZONTAL)
        data_button = wx.Button(self, wx.ALIGN_LEFT, label='Output folder', size=(90, 30))
        data_button.Bind(wx.EVT_BUTTON, self.dataclick)
        self.data_err = wx.StaticText(self, label='Select/Insert the cascade file path')
        self.data_err.SetForegroundColour((255, 0, 0))

        vec_box = BoxMenu(wx.HORIZONTAL)
        vec_button = wx.Button(self, wx.ALIGN_LEFT, label='Vector file', size=(90, 30))
        vec_button.Bind(wx.EVT_BUTTON, self.vecclick)
        self.vec_err = wx.StaticText(self, label='Select/Insert the vector file path')
        self.vec_err.SetForegroundColour((255, 0, 0))

        background_box = BoxMenu(wx.HORIZONTAL)
        background_button = wx.Button(self, wx.ALIGN_LEFT, label='Negative paths', size=(90, 30))
        background_button.Bind(wx.EVT_BUTTON, self.bgclick)
        self.bg_err = wx.StaticText(self, label='Select/Insert a background file path')
        self.bg_err.SetForegroundColour((255, 0, 0))

        pos_box = BoxMenu(wx.HORIZONTAL)
        pos_text = wx.StaticText(self, label='Number of positive images : ')
        self.pos_err = wx.StaticText(self, label='Insert the number of positive images')
        self.pos_err.SetForegroundColour((255, 0, 0))

        neg_box = BoxMenu(wx.HORIZONTAL)
        neg_text = wx.StaticText(self, label='Number of negative images : ')
        self.neg_err = wx.StaticText(self, label='Insert the number of negative images')
        self.neg_err.SetForegroundColour((255, 0, 0))

        stage_box = BoxMenu(wx.HORIZONTAL)
        stage_text = wx.StaticText(self, label='Number of stages : ')
        self.stage_err = wx.StaticText(self, label='Insert the number of stages')
        self.stage_err.SetForegroundColour((255, 0, 0))

        width_box = BoxMenu(wx.HORIZONTAL)
        width_text = wx.StaticText(self, label='Minimum hit rate : ')
        self.width_err = wx.StaticText(self, label='Insert the min hit rate of the classifier')
        self.width_err.SetForegroundColour((255, 0, 0))

        height_box = BoxMenu(wx.HORIZONTAL)
        height_text = wx.StaticText(self, label='False alarm ratio : ')
        self.heigth_err = wx.StaticText(self, label='Insert the max false alarm ratio of the classifier')
        self.heigth_err.SetForegroundColour((255, 0, 0))

        self.data_path = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(300, 30))
        self.vec_path = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(300, 30))
        self.background_path = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(300, 30))
        self.pos = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(70, 30))
        self.neg = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(70, 30))
        self.stage = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(70, 30))
        self.width = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(70, 30))
        self.heigth = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(70, 30))

        data_box.Add(data_button, 0, wx.RIGHT, 94)
        data_box.Add(self.data_path, 0)
        data_box.Add(self.data_err, 0)
        self.data_err.Hide()

        vec_box.Add(vec_button, 0, wx.RIGHT, 94)
        vec_box.Add(self.vec_path, 0)
        vec_box.Add(self.vec_err, 0)
        self.vec_err.Hide()

        background_box.Add(background_button, 0, wx.RIGHT, 94)
        background_box.Add(self.background_path, 0)
        background_box.Add(self.bg_err, 0)
        self.bg_err.Hide()

        pos_box.Add(pos_text, 0, wx.RIGHT, 11)
        pos_box.Add(self.pos, 0)
        pos_box.Add(self.pos_err, 0)
        self.pos_err.Hide()

        neg_box.Add(neg_text, 0, wx.RIGHT, 7)
        neg_box.Add(self.neg, 0)
        neg_box.Add(self.neg_err, 0)
        self.neg_err.Hide()

        stage_box.Add(stage_text, 0, wx.RIGHT, 60)
        stage_box.Add(self.stage, 0)
        stage_box.Add(self.stage_err, 0)
        self.stage_err.Hide()

        width_box.Add(width_text, 0, wx.RIGHT, 60)
        width_box.Add(self.width, 0)
        width_box.Add(self.width_err, 0)
        self.width_err.Hide()

        height_box.Add(height_text, 0, wx.RIGHT, 66)
        height_box.Add(self.heigth, 0)
        height_box.Add(self.heigth_err, 0)
        self.heigth_err.Hide()

        confirm_box = BoxMenu(wx.HORIZONTAL)
        confirm_button = wx.Button(self, wx.ALIGN_CENTER, label='confirm', size=(70, 30))
        confirm_button.Bind(wx.EVT_BUTTON, self.confirmclick)

        confirm_box.Add(confirm_button, 0)

        mainbox.Add(data_box, 0, wx.ALL, 5)
        mainbox.Add(vec_box, 0, wx.ALL, 5)
        mainbox.Add(background_box, 0, wx.ALL, 5)
        mainbox.Add(pos_box, 0, wx.ALL, 5)
        mainbox.Add(neg_box, 0, wx.ALL, 5)
        mainbox.Add(stage_box, 0, wx.ALL, 5)
        mainbox.Add(width_box, 0, wx.ALL, 5)
        mainbox.Add(height_box, 0, wx.ALL, 5)
        mainbox.Add(confirm_box, 0, wx.ALIGN_RIGHT)

        self.SetSizer(mainbox)
        self.Layout()

    def dataclick(self, event):
        data_search = wx.DirDialog(self, 'Choose media directory', '', style=wx.DD_DEFAULT_STYLE)
        data_search.ShowModal()
        path = data_search.GetPath()
        self.data_path.SetValue(path)
        data_search.Destroy()

    def vecclick(self, event):
        vec_search = wx.FileDialog(self, 'Open', '', '', 'Text files (*.vec)|*.vec',
                                    wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        vec_search.ShowModal()
        path = vec_search.GetPath()
        self.vec_path.SetValue(path)
        vec_search.Destroy()

    def bgclick(self, event):
        bg_search = wx.FileDialog(self, 'Open', '', '', 'Text files (*.txt)|*.txt',
                                   wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        bg_search.ShowModal()
        path = bg_search.GetPath()
        self.background_path.SetValue(path)
        bg_search.Destroy()


    def confirmclick(self, event):
        ok = 0

        if not self.data_path.GetValue():
            self.data_err.Show()
            self.data_err.GetParent().Layout()
            ok = 1

        if not self.vec_path.GetValue():
            self.vec_err.Show()
            self.vec_err.GetParent().Layout()
            ok = 1

        if not self.background_path.GetValue():
            self.bg_err.Show()
            self.bg_err.GetParent().Layout()
            ok = 1

        if not self.pos.GetValue():
            self.pos_err.Show()
            self.pos_err.GetParent().Layout()
            ok = 1

        if not self.neg.GetValue():
            self.neg_err.Show()
            self.neg_err.GetParent().Layout()
            ok = 1

        if not self.stage.GetValue():
            self.stage_err.Show()
            self.stage_err.GetParent().Layout()
            ok = 1

        if not self.width.GetValue():
            self.width_err.Show()
            self.width_err.GetParent().Layout()
            ok = 1

        if not self.heigth.GetValue():
            self.heigth_err.Show()
            self.heigth_err.GetParent().Layout()
            ok = 1

        if ok == 1:
            #return
            pass

        self.data_err.Hide()
        self.vec_err.Hide()
        self.bg_err.Hide()
        self.pos_err.Hide()
        self.neg_err.Hide()
        self.stage_err.Hide()
        self.width_err.Hide()
        self.heigth_err.Hide()



        #LicentaBackend.haardetection.detect(self.data_path.GetValue(), self.vec_path.GetValue(),
        #                                    self.background_path.GetValue(), self.pos.GetValue(),
        #                                    self.neg.GetValue(), self.stage.GetValue(),
        #                                    self.width.GetValue(), self.heigth.GetValue(),
        #                                    printfct=panels['output_panel'].printLine)
        #hard codded entry ca sa nu dau click, trebuie schimbat si mai sus la return pass

        global displayed_panel
        panels[displayed_panel].Hide()
        panels['output_panel'].Show()
        panels['output_panel'].GetParent().Layout()
        displayed_panel = 'output_panel'

        LicentaBackend.haardetection.detect(r'C:\Users\Serban\Desktop\LicentaResources\output',
                                            r'C:\Users\Serban\Desktop\LicentaResources\vecf.vec',
                                            r'C:\Users\Serban\Desktop\LicentaResources\negative.txt',
                                            '6', '100', '15', '0.999', '0.5',
                                            printfct=panels['output_panel'].printline)



class RecognitionPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)


class FullDetectionPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)


class TrainCNNPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)


class TrainHaarClPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)


# class RedirectText taken from
# http://www.blog.pythonlibrary.org/2009/01/01/wxpython-redirecting-stdout-stderr/
class RedirectText(object):
    def __init__(self, text):
        self.out = text

    def write(self, string):
        self.out.WriteText(string)


class OutputPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        box = wx.BoxSizer(wx.VERTICAL)

        self.outputctrl = wx.TextCtrl(self, wx.ID_ANY, size=(700, 700), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)

        box.Add(self.outputctrl, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(box)
        self.Layout()

    def printline(self, st):
        redir = RedirectText(self.outputctrl)
        sys.stdout = redir
        print(st)


class CreateSamplesPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        mainbox = wx.BoxSizer(wx.VERTICAL)

        image_box = BoxMenu(wx.HORIZONTAL)
        image_button = wx.Button(self, wx.ALIGN_LEFT, label='Negative Images', size=(100, 30))
        image_button.Bind(wx.EVT_BUTTON, self.imclick)
        self.image_err = wx.StaticText(self, label='Select/Insert a path to the netive images folder')
        self.image_err.SetForegroundColour((255, 0, 0))

        background_box = BoxMenu(wx.HORIZONTAL)
        background_button = wx.Button(self, wx.ALIGN_LEFT, label='Output location', size=(100, 30))
        background_button.Bind(wx.EVT_BUTTON, self.bgclick)
        self.bg_err = wx.StaticText(self, label='Select/Insert path to output folder location')
        self.bg_err.SetForegroundColour((255, 0, 0))

        name_box = BoxMenu(wx.HORIZONTAL)
        name_text = wx.StaticText(self, label='Negative images file name : ')
        self.name_err = wx.StaticText(self, label='Insert the desired name for the output file')
        self.name_err.SetForegroundColour((255, 0, 0))

        confirmbg_box = BoxMenu(wx.HORIZONTAL)
        confirmbg_button = wx.Button(self, wx.ALIGN_CENTER, label='confirm', size=(70, 30))
        confirmbg_button.Bind(wx.EVT_BUTTON, self.confirmbgclick)

        nr_box = BoxMenu(wx.HORIZONTAL)
        nr_text = wx.StaticText(self, label='Number of positive images : ')
        self.nr_err = wx.StaticText(self, label='Insert the number of positive images')
        self.nr_err.SetForegroundColour((255, 0, 0))

        pos_box = BoxMenu(wx.HORIZONTAL)
        pos_button = wx.Button(self, wx.ALIGN_LEFT, label='Positive path', size=(100, 30))
        pos_button.Bind(wx.EVT_BUTTON, self.posclick)
        self.pos_err = wx.StaticText(self, label='Insert the annotations file path')
        self.pos_err.SetForegroundColour((255, 0, 0))

        out_box = BoxMenu(wx.HORIZONTAL)
        out_button = wx.Button(self, wx.ALIGN_LEFT, label='Vector location', size=(100, 30))
        out_button.Bind(wx.EVT_BUTTON, self.outclick)
        self.out_err = wx.StaticText(self, label='Select/Insert path to output folder location')
        self.out_err.SetForegroundColour((255, 0, 0))

        name2_box = BoxMenu(wx.HORIZONTAL)
        name2_text = wx.StaticText(self, label='Name of the new vector file : ')
        self.name2_err = wx.StaticText(self, label='Insert the desired name for the vector file')
        self.name2_err.SetForegroundColour((255, 0, 0))

        confirm_box = BoxMenu(wx.HORIZONTAL)
        confirm_button = wx.Button(self, wx.ALIGN_CENTER, label='Create', size=(70, 30))
        confirm_button.Bind(wx.EVT_BUTTON, self.confirmclick)

        self.image_path = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(300, 30))
        self.bg_path = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(300, 30))
        self.name = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(100, 30))
        self.nr = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(100, 30))
        self.pos = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(300, 30))
        self.out = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(300, 30))
        self.name2 = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(100, 30))

        image_box.Add(image_button, 0, wx.RIGHT, 61)
        image_box.Add(self.image_path, 0)
        image_box.Add(self.image_err, 0)
        self.image_err.Hide()

        background_box.Add(background_button, 0, wx.RIGHT, 61)
        background_box.Add(self.bg_path, 0)
        background_box.Add(self.bg_err, 0)
        self.bg_err.Hide()

        name_box.Add(name_text, 0, wx.RIGHT, 10)
        name_box.Add(self.name, 0)
        name_box.Add(self.name_err, 0)
        self.name_err.Hide()

        confirmbg_box.Add(confirmbg_button, 0)

        nr_box.Add(nr_text, 0, wx.RIGHT, 30)
        nr_box.Add(self.nr, 0)
        nr_box.Add(self.nr_err, 0)
        self.nr_err.Hide()

        pos_box.Add(pos_button, 0, wx.RIGHT, 79)
        pos_box.Add(self.pos, 0)
        pos_box.Add(self.pos_err, 0)
        self.pos_err.Hide()

        out_box.Add(out_button, 0, wx.RIGHT, 80)
        out_box.Add(self.out, 0)
        out_box.Add(self.out_err, 0)
        self.out_err.Hide()

        name2_box.Add(name2_text, 0, wx.RIGHT, 27)
        name2_box.Add(self.name2, 0)
        name2_box.Add(self.name2_err, 0)
        self.name2_err.Hide()

        confirm_box.Add(confirm_button, 0)

        mainbox.Add(image_box, 0, wx.ALL, 5)
        mainbox.Add(background_box, 0, wx.ALL, 5)
        mainbox.Add(name_box, 0, wx.ALL, 5)
        mainbox.Add(confirmbg_box, 0, wx.ALIGN_CENTER)
        mainbox.Add(pos_box, 0, wx.ALL, 5)
        mainbox.Add(out_box, 0, wx.ALL, 5)
        mainbox.Add(name2_box, 0, wx.ALL, 5)
        mainbox.Add(nr_box, 0, wx.ALL, 5)
        mainbox.Add(confirm_box, 0, wx.ALIGN_CENTER)

        self.SetSizer(mainbox)
        self.Layout()

    def imclick(self, event):
        file_search = wx.DirDialog(self, 'Choose media directory', '', style=wx.DD_DEFAULT_STYLE)
        file_search.ShowModal()
        path = file_search.GetPath()
        self.image_path.SetValue(path)
        file_search.Destroy()

    def bgclick(self, event):
        bg_search = wx.DirDialog(self, 'Choose media directory', '', style=wx.DD_DEFAULT_STYLE)
        bg_search.ShowModal()
        path = bg_search.GetPath()
        self.bg_path.SetValue(path)
        bg_search.Destroy()

    def confirmbgclick(self, event):
        ok = 0

        if not self.image_path.GetValue():
            self.image_err.Show()
            self.image_err.GetParent().Layout()
            ok = 1

        if not self.bg_path.GetValue():
            self.bg_err.Show()
            self.bg_err.GetParent().Layout()
            ok = 1

        if not self.name.GetValue():
            self.name_err.Show()
            self.name_err.GetParent().Layout()
            ok = 1

        if ok == 1:
            pass

        self.image_err.Hide()
        self.bg_err.Hide()
        self.name_err.Hide()

        global displayed_panel
        panels[displayed_panel].Hide()
        panels['output_panel'].Show()
        panels['output_panel'].GetParent().Layout()
        displayed_panel = 'output_panel'

        LicentaBackend.createBg.createbg(self.image_path.GetValue(), self.bg_path.GetValue(), self.name.GetValue(),
                                         printfunct=panels['output_panel'].printline)
        #LicentaBackend.createBg.createbg(r'C:\Users\Serban\Desktop\LicentaResources\personneg',
                                         #r'C:\Users\Serban\Desktop\LicentaResources', r'neg',
                                         #printfunct=panels['output_panel'].printline)

    def posclick(self, event):
        pos_search = wx.FileDialog(self, 'Open', '', '', 'Text files (*.txt)|*.txt',
                                   wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        pos_search.ShowModal()
        path = pos_search.GetPath()
        self.pos.SetValue(path)
        pos_search.Destroy()

    def outclick(self, event):
        out_search = wx.DirDialog(self, 'Choose media directory', '', style=wx.DD_DEFAULT_STYLE)
        out_search.ShowModal()
        path = out_search.GetPath()
        self.out.SetValue(path)
        out_search.Destroy()

    def confirmclick(self, event):
        ok = 0
        if not self.nr.GetValue():
            self.nr_err.Show()
            self.nr_err.GetParent().Layout()
            ok = 1

        if not self.pos.GetValue():
            self.pos_err.Show()
            self.pos_err.GetParent().Layout()
            ok = 1

        if not self.out.GetValue():
            self.out_err.Show()
            self.out_err.GetParent().Layout()
            ok = 1

        if not self.name2.GetValue():
            self.name2_err.Show()
            self.name2_err.GetParent().Layout()
            ok = 1

        if ok == 1:
            #return
            pass

        global displayed_panel
        panels[displayed_panel].Hide()
        panels['output_panel'].Show()
        panels['output_panel'].GetParent().Layout()
        displayed_panel = 'output_panel'

        LicentaBackend.vect.create_vec(self.pos.GetValue(), self.out.GetValue(),
                                       self.name.GetValue(), self.nr.GetValue(),
                                       printfunct=panels['output_panel'].printline)


class CropPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        mainbox = wx.BoxSizer(wx.VERTICAL)

        positive_box = BoxMenu(wx.HORIZONTAL)
        positive_button = wx.Button(self, wx.ALIGN_LEFT, label='Positive Images', size=(100, 30))
        positive_button.Bind(wx.EVT_BUTTON, self.posclick)
        self.positive_err = wx.StaticText(self, label='Select/Insert a path to the positive images folder')
        self.positive_err.SetForegroundColour((255, 0, 0))

        output_box = BoxMenu(wx.HORIZONTAL)
        output_button = wx.Button(self, wx.ALIGN_LEFT, label='Output location', size=(100, 30))
        output_button.Bind(wx.EVT_BUTTON, self.outclick)
        self.output_err = wx.StaticText(self, label='Select/Insert path to output folder location')
        self.output_err.SetForegroundColour((255, 0, 0))

        name_box = BoxMenu(wx.HORIZONTAL)
        name_text = wx.StaticText(self, label='Positive images file name : ')
        self.name_err = wx.StaticText(self, label='Insert the desired name for the output file')
        self.name_err.SetForegroundColour((255, 0, 0))

        height_box = BoxMenu(wx.HORIZONTAL)
        height_text = wx.StaticText(self, label='Maximum Window height : ')
        self.height_err = wx.StaticText(self, label='Insert the max window height for the images')
        self.height_err.SetForegroundColour((255, 0, 0))

        resize_box = BoxMenu(wx.HORIZONTAL)
        resize_text = wx.StaticText(self, label='Resize factor : ')
        self.resize_err = wx.StaticText(self, label='Insert the resize factor for the images')
        self.resize_err.SetForegroundColour((255, 0, 0))

        confirm_box = BoxMenu(wx.HORIZONTAL)
        confirm_button = wx.Button(self, wx.ALIGN_CENTER, label='confirm', size=(70, 30))
        confirm_button.Bind(wx.EVT_BUTTON, self.confirmclick)

        self.positive_path = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(300, 30))
        self.output_path = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(300, 30))
        self.name = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(100, 30))
        self.height = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(100, 30))
        self.resize = wx.TextCtrl(self, wx.ALIGN_LEFT, size=(100, 30))

        positive_box.Add(positive_button, 0, wx.RIGHT, 61)
        positive_box.Add(self.positive_path, 0)
        positive_box.Add(self.positive_err, 0)
        self.positive_err.Hide()

        output_box.Add(output_button, 0, wx.RIGHT, 61)
        output_box.Add(self.output_path, 0)
        output_box.Add(self.output_err, 0)
        self.output_err.Hide()

        name_box.Add(name_text, 0, wx.RIGHT, 12)
        name_box.Add(self.name, 0)
        name_box.Add(self.name_err, 0)
        self.name_err.Hide()

        height_box.Add(height_text, 0, wx.RIGHT, 8)
        height_box.Add(self.height, 0)
        height_box.Add(self.height_err, 0)
        self.height_err.Hide()

        resize_box.Add(resize_text, 0, wx.RIGHT, 79)
        resize_box.Add(self.resize, 0)
        resize_box.Add(self.resize_err, 0)
        self.resize_err.Hide()

        confirm_box.Add(confirm_button, 0)

        mainbox.Add(positive_box, 0, wx.ALL, 5)
        mainbox.Add(output_box, 0, wx.ALL, 5)
        mainbox.Add(name_box, 0, wx.ALL, 5)
        mainbox.Add(height_box, 0, wx.ALL, 5)
        mainbox.Add(resize_box, 0, wx.ALL, 5)
        mainbox.Add(confirm_box, 0, wx.ALIGN_CENTER)

        self.SetSizer(mainbox)
        self.Layout()

    def posclick(self, event):
        file_search = wx.DirDialog(self, 'Choose media directory', '', style=wx.DD_DEFAULT_STYLE)
        file_search.ShowModal()
        path = file_search.GetPath()
        self.positive_path.SetValue(path)
        file_search.Destroy()

    def outclick(self, event):
        file_search = wx.DirDialog(self, 'Choose media directory', '', style=wx.DD_DEFAULT_STYLE)
        file_search.ShowModal()
        path = file_search.GetPath()
        self.output_path.SetValue(path)
        file_search.Destroy()

    def confirmclick(self, event):
        ok = 0

        if not self.positive_path.GetValue():
            self.positive_err.Show()
            self.positive_err.GetParent().Layout()
            ok = 1

        if not self.output_path.GetValue():
            self.output_err.Show()
            self.output_err.GetParent().Layout()
            ok = 1

        if not self.name.GetValue():
            self.name_err.Show()
            self.name_err.GetParent().Layout()
            ok = 1

        if not self.height.GetValue():
            self.height_err.Show()
            self.height.GetParent().Layout()
            ok = 1

        if not self.resize.GetValue():
            self.resize_err.Show()
            self.resize_err.GetParent().Layout()
            ok = 1

        if ok == 1:
            pass
        #   return

        self.positive_err.Hide()
        self.output_err.Hide()
        self.name_err.Hide()
        self.height_err.Hide()
        self.resize_err.Hide()

        LicentaBackend.annotation.annotate(self.positive_path.GetValue(), self.output_path.GetValue(),
                                           self.name.GetValue(), self.height.GetValue(), self.resize.GetValue())



app = MainApplication()
app.MainLoop()
