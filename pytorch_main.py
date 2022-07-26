import torch
import torchvision

from pytorch_utils import architecture, get_info, training

if __name__=="__main__":


    get_info.torch_info()
    get_info.gpu_info()

    print()

    train_loader, test_loader = training.get_dataloaders(download=True,
                                                    batch_size=64,
                                                    num_workers=0,
                                                    pin_memory=False)

    model = architecture.BasicClassif().to("cuda")
    loss = torch.nn.CrossEntropyLoss().to("cuda")
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    for epoch in range(1, 6):
        training.train(model, torch.device('cuda'), train_loader, optimizer, loss, epoch)
        training.test(model, torch.device('cuda'), test_loader, loss)