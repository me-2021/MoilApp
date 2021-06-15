import json


class Camera:

    def __init__(self, parameter_path, label_width, label_height):

        with open(parameter_path) as f:
            self.moil_parameter = json.load(f)

        print("\nCamera.__init__(): self.moil_parameter is ", self.moil_parameter)

        self.org_center_x = self.moil_parameter["iCx"]
        self.org_center_y = self.moil_parameter["iCy"]
        self.org_width = self.moil_parameter["imageWidth"]
        self.org_height = self.moil_parameter["imageHeight"]
        self.org_aspect_ratio = self.org_height / self.org_width

        self.label_align = None
        self.label_center_x = None
        self.label_center_y = None
        self.label_width = label_width
        self.label_height = label_height
        self.label_aspect_ratio = self.label_height / self.label_width

        self.ratio_calibration2org = self.moil_parameter["calibrationRatio"]
        self.ratio_ort2calibration = 1 / self.ratio_calibration2org
        self.ratio_label2org = None
        self.ratio_org2label = None

        self.label_clicked_time = 0

        self.set_label_align()
        self.set_ratio()
        self.set_label_center()

    def set_label_align(self):
        if self.org_aspect_ratio >= self.label_aspect_ratio:
            self.label_align = "height"
        elif self.org_aspect_ratio < self.label_aspect_ratio:
            self.label_align = "width"

    def set_ratio(self):
        if self.label_align == "height":
            self.ratio_org2label = self.label_height / self.org_height
            self.ratio_label2org = self.org_height / self.label_height

        elif self.label_align == "width":
            self.ratio_org2label = self.label_width / self.org_width
            self.ratio_label2org = self.org_width / self.label_width

    def set_label_center(self):
        self.label_center_x = self.org_center_x * self.ratio_org2label
        self.label_center_y = self.org_center_y * self.ratio_org2label
