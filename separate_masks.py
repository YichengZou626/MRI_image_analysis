#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 22:52:38 2021

@author: xychen
"""

import numpy as np
import SimpleITK as sitk

label = sitk.ReadImage('./tissue_map_relabeled_edited.nii.gz')

spacing = label.GetSpacing()
orientation = label.GetDirection()
origin = label.GetOrigin()

array = sitk.GetArrayFromImage(label)

new_array = np.zeros_like(array, dtype=np.float32)
new_array[np.where(array == 3)] = 1

new_label = sitk.GetImageFromArray(new_array)

new_label.SetSpacing(spacing)
new_label.SetDirection(orientation)
new_label.SetOrigin(origin)

sitk.WriteImage(new_label, './tissue_map_relabeled_edited_csf.nii.gz')


new_array = np.zeros_like(array, dtype=np.float32)
new_array[np.where(np.logical_or(array == 1, array == 2))] = 1

new_label = sitk.GetImageFromArray(new_array)

new_label.SetSpacing(spacing)
new_label.SetDirection(orientation)
new_label.SetOrigin(origin)

sitk.WriteImage(new_label, './tissue_map_relabeled_edited_gm_and_wm.nii.gz')

new_array = np.zeros_like(array, dtype=np.float32)
new_array[np.where(array == 2)] = 1

new_label = sitk.GetImageFromArray(new_array)

new_label.SetSpacing(spacing)
new_label.SetDirection(orientation)
new_label.SetOrigin(origin)

sitk.WriteImage(new_label, './tissue_map_relabeled_edited_wm_only.nii.gz')


new_array = np.zeros_like(array, dtype=np.float32)
new_array[np.where(array == 1)] = 1

new_label = sitk.GetImageFromArray(new_array)

new_label.SetSpacing(spacing)
new_label.SetDirection(orientation)
new_label.SetOrigin(origin)

sitk.WriteImage(new_label, './tissue_map_relabeled_edited_gm_only.nii.gz')



new_array = np.zeros_like(array, dtype=np.float32)
new_array[np.where(array > 0)] = 1

new_label = sitk.GetImageFromArray(new_array)

new_label.SetSpacing(spacing)
new_label.SetDirection(orientation)
new_label.SetOrigin(origin)

sitk.WriteImage(new_label, './tissue_map_relabeled_edited_all.nii.gz')
