# ---------------Name: StarDEM -------------------
# ------------Author: Chengshun Shang-------------
# -----------------Date: 04-01-2022---------------
# ---------------License : BSD license------------

from PreProcess.getInitialParticleData import getInitialParticleData
from PostProcess.PostProcess import PostProcess

class TheMainProcess():

    def __init__(self) -> None:
        
        self.myDEMData = getInitialParticleData()
        self.myDEMPost = PostProcess()

        self.i_run_time = 0.0
        self.aim_run_time = 1.0
        self.time_step = 1e-5
        self.L = 0.005
        self.W = 0.005
        self.T = 0.005
        self.r = 0.0001
        self.initial_particle_number = 5
        self.is_round = False   #you should be careful when you set this parameters :)

        #for creating membrane layer
        self.H = 0.1
        self.r_in = 0.025
        self.r_m = 0.001
        self.p_id_ini = 30048

        #for reading mdpa file
        self.aim_mdpa_file_name = '3D-danzhou-R-1.5-1.txt'

        #for set particle group ID
        self.sample_height = 0.108
        self.sample_width  = 0.054
        self.joint_angle   = 83.0
        self.joint_width_1 = 0.006  # this is the joint width
        self.joint_width_2 = 0.010  # this is the main rock width
        self.joint_point = [0.0, 0.054, 0.0]

        #for divide sample into 3 parts
        self.width_1 = 0.004
        self.width_2 = 0.04

    # running functions
    def run(self):

        #self.myDEMData.creat_disk(self.L, self.W, self.r, self.is_round)
        #self.myDEMData.creat_sphere(self.L, self.W, self.T, self.r, self.is_round)
        #self.myDEMData.creat_sphere_adaptive(self.L, self.W, self.T, self.initial_particle_number, self.is_round)
        #self.myDEMData.creat_membrane(self.H, self.r_in, self.r_m, self.p_id_ini)
        #self.myDEMData.getParticleDataFromMdpa(self.aim_mdpa_file_name)
        #self.myDEMData.getParticleDataFromEDEM(self.aim_mdpa_file_name)
        #self.myDEMData.setParticleGroupID(self.sample_height, self.sample_width, self.joint_angle, self.joint_width_1, self.joint_width_2, self.myDEMData.p_pram_list)
        #self.myDEMData.setParticleGroupIDSingle(self.sample_height, self.joint_angle, self.joint_width_1, self.myDEMData.p_pram_list)
        #self.myDEMData.setParticleGroupIDSingleSlim(self.joint_angle, self.joint_point, self.myDEMData.p_pram_list)
        #self.myDEMData.setParticleGroupIDSimple(self.width_1, self.width_2, self.myDEMData.p_pram_list)
        #self.myDEMData.creat_aluminium(self.r, self.is_round)
        self.myDEMData.creat_hcp(self.L, self.W, self.T, self.r, self.is_round)
        self.main_cicle()
        #self.plot_results()
        self.myDEMPost.WriteOutParaview(self.myDEMData)
        self.myDEMPost.WriteOutGIDData(self.myDEMData)
        #self.myDEMPost.WriteOutGIDDataNonCohesive(self.myDEMData)

    # cicle for force and information update
    def main_cicle(self):

        while self.i_run_time < self.aim_run_time:
            # traverse all the 
            for p_pram_dict in self.myDEMData.p_pram_list:
                
                #force_cal(p_pram_dict["p_x"], p_pram_dict["p_y"], p_pram_dict["radius"], p_pram_dict["p_v_x"], p_pram_dict["p_v_y"])
                print("%s\t" % p_pram_dict)

            #self.i_run_time += self.time_step
            break

# TO DO: constitutive model
# def force_cal(p_x, p_y, radius, p_v_x, p_v_y):
    
if __name__ == "__main__":

    TestDEM = TheMainProcess()
    TestDEM.run()
