clear all;
EIGENFACE = dlmread('SaveData/EIGEN_TEST_DATA.txt');
FISHERFACE = dlmread('SaveData/FISHER_TRAINER.txt');
LBPH_RAD = dlmread('SaveData/LBPH/LBPH_PIXEL_RADIUS.txt');
LBPH_NEIG = dlmread('SaveData/LBPH/LBPH_NEIGHBOURS.txt');
LBPH_CELL = dlmread('SaveData/LBPH/LBPH_CELLS.txt');

path = 'Plots/SAM_'
% 1920 x 1080
POX = -1920;
POY = 1080-300;
figure('OuterPosition',[POX, POY, 1200, 300])
subplot(1,2,1)
    p = plot(EIGENFACE(:, 1), 'Color',[0,0.7,0.9])
    title('ID on EigenFace against Number of Components')
    ylabel('ID')
    xlabel('Number of Components')
    p.LineWidth = 1
    ylim([15 25])
    xlim([1 200 ])
    %print(strcat(path,'EIGEN_ID'), '-dpng')


subplot(1,2,2)
    p = plot(EIGENFACE(:, 2), 'red')
    p.LineWidth = 1
    title('Confidence on EigenFace against Number of Components')
    ylabel('Confidence')
    xlabel('Number of Components')
    xlim([1 200 ])
    print(strcat(path,'EIGEN'), '-dpng')
%-------------------------------------------------------------------------------------
%-------------------------------------------------------------------------------------
POX = -1920;
POY = POY - 300
figure('OuterPosition',[POX, POY, 1200, 300])
subplot(1,2,1)
    p = plot(FISHERFACE(:, 1), 'Color',[0,0.7,0.9])
    title('ID on FisherFace Recognition against Number of Components')
    ylabel('ID')
    xlabel('Number of Components')
    p.LineWidth = 1
    ylim([15 25])
    xlim([1 200 ])
    %print(strcat(path,'FISHER_ID'), '-dpng')
    
subplot(1,2,2)
    p = plot(FISHERFACE(:, 2), 'red')
    p.LineWidth = 1
    title('Confidence on FisherFace against Number of Components')
    ylabel('Confidence')
    xlabel('Number of Components')
    ylim([0 1500])
    xlim([1 200 ])
    print(strcat(path,'FISHER'), '-dpng')
%-------------------------------------------------------------------------------------
%                      Local Binary Pattern Histogram
%-------------------------------------------------------------------------------------
POX = 0
POY = 1080-300;

figure('OuterPosition',[POX, POY, 1200, 300])
subplot(1,2,1)
    p = plot(LBPH_RAD(:, 1), 'Color',[0,0.7,0.9])
    p.LineWidth = 1
    title('ID on LBPHFace Recognition against Radius from the central pixel')
    ylabel('ID')
    xlabel('Radius from the central pixel')
    ylim([15 25])
    xlim([1 54 ])
    
subplot(1,2,2)
    p = plot(LBPH_RAD(:, 2), 'red')
    p.LineWidth = 1
    title('Confidance on LBPHFace Recognition against Radius from the central pixel')
    ylabel('ID')
    xlabel('Radius from the central pixel')
    xlim([1 54 ])
    print(strcat(path,'LBPH_RAD'), '-dpng')
%-------------------------------------------------------------------------------------
    
POY = POY - 300


figure('OuterPosition',[POX, POY, 1200, 300])
subplot(1,2,1)
    p = plot(LBPH_NEIG(:, 1), 'Color',[0,0.7,0.9])
    p.LineWidth = 1
    title('ID on LBPHFace Recognition against the Number of Neighbours')
    ylabel('ID')
    xlabel('Number of Neighbours')
    ylim([15 25])
    xlim([1 13 ])
    
subplot(1,2,2)
    p = plot(LBPH_NEIG(:, 2), 'red')
    p.LineWidth = 1
    title('Confidance on LBPHFace Recognition against the Number of Neighbours')
    ylabel('ID')
    xlabel('Number of Neighbours')
    xlim([1 13 ])
    print(strcat(path,'LBPH_N'), '-dpng')


%-------------------------------------------------------------------------------------
POY = POY - 300


figure('OuterPosition',[POX, POY, 1200, 300])
subplot(1,2,1)
    p = plot(LBPH_CELL(:, 1), 'Color',[0,0.7,0.9])
    p.LineWidth = 1
    title('ID on LBPHFace Recognition when against Number of Cells','FontSize', 10)
    ylabel('ID')
    xlabel('Number of Cells')
    ylim([15 25])
    xlim([1 50 ])



subplot(1,2,2)
    p = plot(LBPH_CELL(:, 2), 'red')
    p.LineWidth = 1
    title('Confidance on LBPHFace Recognition against the Number of Cells')
    ylabel('ID')
    xlabel('Number of Cells')
    xlim([1 50 ])
    print(strcat(path,'LBPH_C'), '-dpng')


% close all