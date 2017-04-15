figure
plot(Componen, ID, 'Color',[0,0.7,0.9])

title('Returned ID on EigenFace Recognition While Changing Number of Components')
ylabel('ID')
xlabel('Number of Components')
ylim([15 25])
xlim([1 200 ])

figure

plot(Componen, Confidence, 'Color',[0,0.7,0.9])

title('Returned Confidence on EigenFace While Changing Number of Components')
ylabel('Confidence')
xlabel('Number of Components')
%ylim([15 25])
xlim([1 200 ])
%-------------------------------------------------------------------------------------
%-------------------------------------------------------------------------------------

figure

plot(Componen, FID, 'Color',[0,0.7,0.9])

title('Returned ID on FisherFace Recognition While Changing Number of Components')
ylabel('ID')
xlabel('Number of Components')
ylim([15 25])
xlim([1 200 ])

figure

plot(Componen, FConf, 'red')

title('Returned Confidence on FisherFace While Changing Number of Components')
ylabel('Confidence')
xlabel('Number of Components')
ylim([0 1500])
xlim([1 200 ])

%-------------------------------------------------------------------------------------
%-------------------------------------------------------------------------------------

figure

plot(LID, 'Color',[0,0.7,0.9])

title('Returned ID on LBPHFace Recognition While Changing Radius from the central pixel')
ylabel('ID')
xlabel('Radius from the central pixel')
ylim([15 25])
xlim([1 50 ])

figure

plot(LConf, 'red')

title('Returned Confidance on LBPHFace Recognition While Changing Radius from the central pixel')
ylabel('ID')
xlabel('Radius from the central pixel')
%ylim([15 25])
xlim([1 50 ])

%-------------------------------------------------------------------------------------
figure

plot(LNID, 'Color',[0,0.7,0.9])

title('Returned ID on LBPHFace Recognition While Changing the Number of Neighbours')
ylabel('ID')
xlabel('Number of Neighbours')
ylim([15 25])
xlim([1 13 ])

figure

plot(LNConf, 'red')

title('Returned Confidance on LBPHFace Recognition While Changing the Number of Neighbours')
ylabel('ID')
xlabel('Number of Neighbours')
%ylim([15 25])
xlim([1 13 ])

%-------------------------------------------------------------------------------------
figure

plot(LCID, 'Color',[0,0.7,0.9])

title('Returned ID on LBPHFace Recognition While Changing the Number of Cells')
ylabel('ID')
xlabel('Number of Cells')
ylim([15 25])
xlim([1 50 ])

figure

plot(LCConf, 'red')

title('Returned Confidance on LBPHFace Recognition While Changing the Number of Cells')
ylabel('ID')
xlabel('Number of Cells')
%ylim([15 25])
xlim([1 50 ])


