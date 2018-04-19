"""         Script variabler                                      """

global RunningCleanup,Createmodel,Savemodel,numCPU

RunningCleanup = 1
Createmodel = 1
Savemodel = 1
#numCPU = 1
numCPU = multiprocessing.cpu_count()


"""Analyse varialbler       """
global Runjobs,linearAnalysis,nonLinearAnalysis,Increments,Dampening,Stabl_Magn, Atapt_Damp_Ratio,Singlepin,tripplepin,MaterialDens

Runjobs = 1                             #   ON/OFF Start analyser or create .inp
linearAnalysis = 0                      #   ON/OFF Linear analyse for stiffness
nonLinearAnalysis = 1                   #   ON/OFF non-linear analyse for strength
Increments = {'maxNum': 100, 'initial': 1e-02, 'min': 1e-4, 'max': 1e-1}

Dampening = 1
Stabl_Magn =2e-4
Atapt_Damp_Ratio = 0.05

Singlepin = 1                               #   Randbetingelse:    Laaser hjornenode mot forskyvning i 3 retninger
tripplepin = 0                              #   Randbetingelse:    Laaser to noder mot forskyvning. En sentrert kantnode i 2 retninger og midtnode i 1 retning

MaterialDens  = 0                           #Material Density


"""         Test variabler                                      """

global noFibertest,Fibervariation,rmean,Rstdiv,Interface,rinterface,ElementInterfaceT,FiberSirkelResolution,meshsize

noFibertest = 0                                     # ON/OFF Fiber i modellen.
Fibervariation = 1                                  # ON/OFF variasjon fiberradius. Mean and standard div. Kan paavirke Vf i endelig model.

rmean = 8.7096                              # Gjennomsnittradius pa fiber
Rstdiv = 0.6374                             # OStandard avvik fra gjennomsnittsradius

Interface = 1                                   # ON/OFF CohesiveInterface
rinterface = 0.0001                              # Interfacetykkelse ved modellering. Verdi er relativ til radius.    0.01 = 1%
ElementInterfaceT = 0                  # Interfacetykkelse paa elementene.  Verdi er relativ til radius.

# Meshsize
FiberSirkelResolution =  24                                 # Meshresolution pa Fiber omkrets. 2*pi/FiberSirkelResolution
meshsize = rmean * 2 * pi / FiberSirkelResolution           # Meshsize fra resolution paa interface paa fiberomkrets

