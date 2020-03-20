
%% Prepare Data
path = 'path/to/images';
fnames = dir(path);
train_data = [];
for i = 3:length(images)
    train_data(:,:,:,i-2) = imread([path  '/' images(i).name]);
end
train_data = train_data./255;
label_file = fopen('train_labels.txt');
label_data = textscan(label_file,'%s');
fclose(label_file);
train_labels = categorical(string(label_data{:}));

%% Prepare Network

layers=[
    imageInputLayer([150,150,3])
    convolution2dLayer(10,10)
    batchNormalizationLayer
    reluLayer
    maxPooling2dLayer(4,'Stride',4)
    convolution2dLayer(8,16)
    batchNormalizationLayer
    reluLayer
    maxPooling2dLayer(2,'Stride',4)
    convolution2dLayer(4,32)
    batchNormalizationLayer
    reluLayer
    maxPooling2dLayer(2,'Stride',4)
    fullyConnectedLayer(100)
    fullyConnectedLayer(10)
    softmaxLayer
    classificationLayer];

options = trainingOptions('sgdm',...
    'InitialLearnRate', 1e-4 ,...
    'MaxEpochs', 50 ,...
    'Shuffle', 'every-epoch', ...
    'Verbose',true,...
    'Plots', 'training-progress',...
    'MiniBatchSize',128,...
    'L2Regularization',0.001);

%% Train the network

net = trainNetwork(train_data,train_labels,layers,options);
