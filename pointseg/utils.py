import numpy as np

import torch


def img_normalize(x):
    return ((x - torch.min(x)) / (torch.max(x) - torch.min(x))).view(
                1, x.size()[0], x.size()[1]
            )

def visualize_seg(label_map, cfg, one_hot=False):
    cmap = np.array(cfg['class-cmap'])
    n_cls = len(cfg['classes'])

    if one_hot:
        label_map = np.argmax(label_map, axis=-1)

    out = torch.zeros([label_map.size()[0], label_map.size()[1], label_map.size()[2], 3], dtype=torch.float64)

    for l in range(1, n_cls):
        out[label_map==l, :] = torch.from_numpy(cmap[l])

    return out.transpose(2,3).transpose(1,2)