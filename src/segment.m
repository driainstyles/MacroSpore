close all;
clear all;
im = double(imread('Overlay.png'));
% Delete empty blue channel
im(:,:,3) = [];
[nr,nc,~] = size(im);
X = reshape(im,nr*nc,2)';

% Define two distance functions
deuc = @(d,c) mean((c-d)'*(c-d));
dcos = @(d,c) acos((d'*c)/(norm(c)*norm(d)));

% Do the clustering
[cmean,ClusterIndex]=kmeans(X,4,deuc);
plotClusterImages(ClusterIndex,nr,nc);
[cmean,ClusterIndex]=kmeans(X,4,dcos);
plotClusterImages(ClusterIndex,nr,nc);
