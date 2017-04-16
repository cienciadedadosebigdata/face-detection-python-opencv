% clear all;
% EIGENFACE = dlmread('SaveData/EIGEN_TRAINER.txt');
% FISHERFACE = dlmread('SaveData/FISHER_TRAINER.txt');
% LBPH_RAD = dlmread('SaveData/LBPH/LBPH_PIXEL_RADIUS.txt');
% LBPH_NEIG = dlmread('SaveData/LBPH/LBPH_NEIGHBOURS.txt');
% LBPH_CELL = dlmread('SaveData/LBPH/LBPH_CELLS.txt');

path = 'Plots/ME4_'
% 1920 x 1080
POX = -1920;
POY = 1080-300;
figure('OuterPosition',[POX, POY, 610, 300])
    p = plot(EIGENFACE(:, 1), 'Color',[0,0.7,0.9])
    title('ID on EigenFace against Number of Components','FontSize', 10)
    ylabel('ID')
    xlabel('Number of Components')
    p.LineWidth = 1
    ylim([15 25])
    xlim([1 200 ])
    print(strcat(path,'EIGEN_ID'), '-dpng')

POX = POX + 610;
figure('OuterPosition',[POX, POY, 610, 300])
    p = plot(EIGENFACE(:, 2), 'red')
    p.LineWidth = 1
    title('Confidence on EigenFace against Number of Components','FontSize', 10)
    ylabel('Confidence')
    xlabel('Number of Components')
    xlim([1 200 ])
    print(strcat(path,'EIGEN_CONF'), '-dpng')
%-------------------------------------------------------------------------------------
%-------------------------------------------------------------------------------------
POX = -1920;
POY = POY - 300
figure('OuterPosition',[POX, POY, 610, 300])
    p = plot(FISHERFACE(:, 1), 'Color',[0,0.7,0.9])
    title('ID on FisherFace Recognition against Number of Components','FontSize', 10)
    ylabel('ID')
    xlabel('Number of Components')
    p.LineWidth = 1
    ylim([15 25])
    xlim([1 200 ])
    print(strcat(path,'FISHER_ID'), '-dpng')
POX = POX + 610;    
figure('OuterPosition',[POX, POY, 610, 300])
    p = plot(FISHERFACE(:, 2), 'red')
    p.LineWidth = 1
    title('Confidence on FisherFace against Number of Components','FontSize', 10)
    ylabel('Confidence')
    xlabel('Number of Components')
    ylim([0 1500])
    xlim([1 200 ])
    print(strcat(path,'FISHER_CONF'), '-dpng')
%-------------------------------------------------------------------------------------
%                      Local Binary Pattern Histogram
%-------------------------------------------------------------------------------------
POX = POX + 610
POY = 1080-300;

figure('OuterPosition',[POX, POY, 610, 300])
    p = plot(LBPH_RAD(:, 1), 'Color',[0,0.7,0.9])
    p.LineWidth = 1
    title('ID on LBPHFace Recognition against Radius from the central pixel','FontSize', 10)
    ylabel('ID')
    xlabel('Radius from the central pixel')
    ylim([15 25])
    xlim([1 54 ])
    print(strcat(path,'LBPH_ID'), '-dpng')
    
POX = POX + 610
figure('OuterPosition',[POX, POY, 610, 300])
    p = plot(LBPH_RAD(:, 2), 'red')
    p.LineWidth = 1
    title('Confidance on LBPHFace Recognition against Radius from the central pixel','FontSize', 10)
    ylabel('ID')
    xlabel('Radius from the central pixel')
    xlim([1 54 ])
    print(strcat(path,'LBPH_CONF'), '-dpng')
%-------------------------------------------------------------------------------------
    
POY = POY - 300
POX = POX - 610

figure('OuterPosition',[POX, POY, 610, 300])
    p = plot(LBPH_NEIG(:, 1), 'Color',[0,0.7,0.9])
    p.LineWidth = 1
    title('ID on LBPHFace Recognition against the Number of Neighbours','FontSize', 10)
    ylabel('ID')
    xlabel('Number of Neighbours')
    ylim([15 25])
    xlim([1 13 ])
    print(strcat(path,'LBPH_N_ID'), '-dpng')
    
POX = POX + 610
figure('OuterPosition',[POX, POY, 610, 300])
    p = plot(LBPH_NEIG(:, 2), 'red')
    p.LineWidth = 1
    title('Confidance on LBPHFace Recognition against the Number of Neighbours','FontSize', 10)
    ylabel('ID')
    xlabel('Number of Neighbours')
    xlim([1 13 ])
    print(strcat(path,'LBPH_N_CONF'), '-dpng')


%-------------------------------------------------------------------------------------
POY = POY - 300
POX = POX - 610
figure('OuterPosition',[POX, POY, 610, 300])
    p = plot(LBPH_CELL(:, 1), 'Color',[0,0.7,0.9])
    p.LineWidth = 1
    title('ID on LBPHFace Recognition against the Number of Cells','FontSize', 10)
    ylabel('ID')
    xlabel('Number of Cells')
    ylim([15 25])
    xlim([1 50 ])
    print(strcat(path,'LBPH_C_ID'), '-dpng')


POX = POX + 610
figure('OuterPosition',[POX, POY, 610, 300])
    p = plot(LBPH_CELL(:, 2), 'red')
    p.LineWidth = 1
    title('Confidance on LBPHFace Recognition against the Number of Cells','FontSize', 10)
    ylabel('ID')
    xlabel('Number of Cells')
    xlim([1 50 ])
    print(strcat(path,'LBPH_C_CONF'), '-dpng')


% close all