import my_model.RC_GAN as RC
import my_model.FC_GAN as FC
import torch
class model_loader:
    def __init__(self,model_type,d_load_path,g_load_path):
        self.model = model_type
        self.d_load_path = d_load_path
        self.g_load_path = g_load_path

    def discriminator(self):
        if self.model == 'FC_GAN':
            D = FC.discriminator()
        elif self.model == "RC_GAN":
            D = RC.discriminator()
        D.load_state_dict(torch.load(self.d_load_path))
        return D

    def generator(self):
        if self.model == 'FC_GAN':
            G = FC.generator()
        elif self.model == "RC_GAN":
            G = RC.generator()
        G.load_state_dict(torch.load(self.g_load_path))
        return G

