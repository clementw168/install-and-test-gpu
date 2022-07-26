import torch

class BasicClassif(torch.nn.Module):
    def __init__(self):
        super(BasicClassif, self).__init__()
        self.fc1 = torch.nn.Linear(28*28, 128)
        self.fc2 = torch.nn.Linear(128, 10)
        self.dp = torch.nn.Dropout(0.2)

    def forward(self, x):
        x = x.view(-1, 28*28)
        x = self.fc1(x)
        x = torch.relu(x)
        x = self.dp(x)
        x = self.fc2(x)
        return x