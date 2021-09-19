import math
import time

import torch
from torch.autograd import Variable
from torch.utils.data import TensorDataset


class KDE():
    def __init__(self, samples, num_attributes):
        self.H = torch.rand(num_attributes)
        self.H = Variable(self.H, requires_grad=True)
        self.sample = samples
        self.num_attributes = num_attributes

    def train(self, train_predicates, cardinalities, total_card, batch_size, num_epochs):
        num_sample = len(self.sample)
        predicates_lower = torch.FloatTensor([[pre[i] for i in range(0, len(pre), 2)] for pre in train_predicates])
        predicates_upper = torch.FloatTensor([[pre[i] for i in range(1, len(pre), 2)] for pre in train_predicates])
        cardinalities = torch.FloatTensor(cardinalities) / total_card
        samples = torch.FloatTensor(self.sample)
        optimizer = torch.optim.Adam([self.H], lr=0.001)
        total_size = len(train_predicates)
        split_idx = int(0.8 * total_size)
        train_dataset = TensorDataset(predicates_lower[:split_idx], predicates_upper[:split_idx],
                                      cardinalities[:split_idx])
        validate_dataset = TensorDataset(predicates_lower[split_idx:], predicates_upper[split_idx:],
                                         cardinalities[split_idx:])
        train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        validate_loader = torch.utils.data.DataLoader(validate_dataset, batch_size=batch_size, shuffle=True)
        train_start_time = time.time()
        for epoch in range(num_epochs):
            for i, (lower, upper, targets) in enumerate(train_loader, 0):
                optimizer.zero_grad()
                ress = 0.0
                for sample in samples:
                    res = 1.0
                    for j in range(self.H.shape[0]):
                        res *= (torch.erf((upper[:, j] - sample[j]) / (math.sqrt(2) * self.H[j])) - torch.erf(
                            (lower[:, j] - sample[j]) / (math.sqrt(2) * self.H[j])))
                    ress += res / (2 ** num_attributes)
                loss = torch.nn.functional.mse_loss(ress, targets)
                print(f'Training Loss: {loss}')
                loss.backward()
                optimizer.step()
        train_end_time = time.time()
        print(f'Training Time: {train_end_time - train_start_time}s')

        mses = []
        qerrors = []
        for i, (lower, upper, targets) in enumerate(validate_loader, 0):
            ress = 0.0
            for sample in samples:
                res = 1.0
                for j in range(self.H.shape[0]):
                    res *= (torch.erf((upper[:, j] - sample[j]) / (math.sqrt(2) * self.H[j])) - torch.erf(
                        (lower[:, j] - sample[j]) / (math.sqrt(2) * self.H[j])))
                ress += res / (2 ** num_attributes)
            mse = (ress - targets) ** 2
            qerror = torch.max(ress, targets) / torch.max(torch.zeros_like(ress) + 1e-5,
                                                          (torch.min(ress, targets) + 1e-5))
            mses.append(mse)
            qerrors.append(qerror)
        qerrors = torch.cat(qerrors).detach().numpy()
        mses = torch.cat(mses).detach().numpy()
        print(f'Validate Mean Q-error: {qerrors.mean()}')
        print(f'Validate Median Q-error: {np.median(qerrors)}')
        print(f'Validate Max Q-error: {qerrors.max()}')
        print(f'Validate 90th Q-error: {np.percentile(qerrors, 90)}')
        print(f'Validate 95th Q-error: {np.percentile(qerrors, 95)}')
        print(f'Validate 99th Q-error: {np.percentile(qerrors, 99)}')
        print(f'Validate MSE: {mses.mean()}')

    def test(self, test_predicates, cardinalities, total_card):
        predicates_lower = torch.FloatTensor([[pre[i] for i in range(0, len(pre), 2)] for pre in test_predicates])
        predicates_upper = torch.FloatTensor([[pre[i] for i in range(1, len(pre), 2)] for pre in test_predicates])
        cardinalities = torch.FloatTensor(cardinalities) / total_card
        samples = torch.FloatTensor(self.sample)
        test_dataset = TensorDataset(predicates_lower, predicates_upper, cardinalities)
        test_loader = torch.utils.data.DataLoader(test_dataset)
        start_time = time.time()
        mses = []
        qerrors = []
        for i, (lower, upper, targets) in enumerate(test_loader, 0):
            ress = 0.0
            for sample in samples:
                res = 1.0
                for j in range(self.H.shape[0]):
                    res *= (torch.erf((upper[:, j] - sample[j]) / (math.sqrt(2) * self.H[j])) - torch.erf(
                        (lower[:, j] - sample[j]) / (math.sqrt(2) * self.H[j])))
                ress += res / (2 ** num_attributes)
            mse = (ress - targets) ** 2
            qerror = torch.max(ress, targets) / torch.max(torch.zeros_like(ress) + 1e-5,
                                                          (torch.min(ress, targets) + 1e-5))
            mses.append(mse)
            qerrors.append(qerror)
        end_time = time.time()
        print(f'Test Time: {end_time - start_time}')
        qerrors = torch.cat(qerrors).detach().numpy()
        mses = torch.cat(mses).detach().numpy()
        print(f'Mean Q-error: {qerrors.mean()}')
        print(f'Median Q-error: {np.median(qerrors)}')
        print(f'Max Q-error: {qerrors.max()}')
        print(f'90th Q-error: {np.percentile(qerrors, 90)}')
        print(f'95th Q-error: {np.percentile(qerrors, 95)}')
        print(f'99th Q-error: {np.percentile(qerrors, 99)}')
        print(f'MSE: {mses.mean()}')


if __name__ == '__name__':
    train_predicates = [[0.1, 0.3, 0.4, 0.5],
                        [0.3, 0.6, 0.7, 0.8],
                        [0.1, 0.4, 0.9, 1.0],
                        [0.2, 0.3, 0.7, 0.8],
                        [0.4, 0.6, 0.5, 0.6]]
    test_predicates = [[0.1, 0.3, 0.5, 0.7],
                       [0.1, 0.4, 0.6, 0.7]]
    train_cardinalities = [20, 30, 90, 15, 31]
    test_cardinalities = [30, 40]
    sample = [[0.15, 0.35], [0.35, 0.55], [0.45, 0.25], [0.65, 0.25], [0.85, 0.15], [0.55, 0.78]]
    num_attributes = 2
    num_epochs = 1000
    total_card = 200
    batch_size = 10
    kde = KDE(samples=sample, num_attributes=num_attributes)
    kde.train(train_predicates, train_cardinalities, total_card, batch_size, num_epochs)
    kde.test(test_predicates, test_cardinalities, total_card)
