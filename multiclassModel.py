from torch import nn
class multiclassModel(nn.Module):
    def __init__(self,input_features,output_features,hidden_units=8):
        super().__init__()
        
        self.linear_layers_stack = nn.Sequential(
            nn.Linear(in_features=input_features,out_features=hidden_units),
            nn.ReLU(),
            nn.Linear(in_features=hidden_units,out_features=hidden_units),
            # nn.ReLU(),
            # nn.Linear(in_features=hidden_units,out_features=hidden_units),
            nn.ReLU(),
            nn.Linear(in_features=hidden_units,out_features=output_features),
            )
    def forward(self, x):
        return self.linear_layers_stack(x)
        
    