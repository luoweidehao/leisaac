from pathlib import Path

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

from leisaac.utils.constant import ASSETS_ROOT


"""Configuration for the SO101 Follower Robot."""
SO101_FOLLOWER_ASSET_PATH = Path(ASSETS_ROOT)/"robots"/"so101_follower.usd"

SO101_FOLLOWER_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=str(SO101_FOLLOWER_ASSET_PATH),
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=4,
            fix_root_link=True,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(2.2, -0.61, 0.89),
        rot=(0.0, 0.0, 0.0, 1.0),
        joint_pos={
            "shoulder_pan": 0.0,
            "shoulder_lift": 0.0,
            "elbow_flex": 0.0,
            "wrist_flex": 0.0,
            "wrist_roll": 0.0,
            "gripper": 0.0
        }
    ),
    actuators={
        "sts3215": ImplicitActuatorCfg(
            joint_names_expr=[".*"],
            effort_limit_sim=1,
            velocity_limit_sim=10,
            stiffness=17.8,
            damping=0.60,
        )
    },
    soft_joint_pos_limit_factor=1.0,
)

SO101_FOLLOWER_USD_JOINT_LIMLITS = {
    "shoulder_pan": (-110.0, 110.0),
    "shoulder_lift": (-100.0, 100.0),
    "elbow_flex": (-100.0, 90.0),
    "wrist_flex": (-95.0, 95.0),
    "wrist_roll": (-160.0, 160.0),
    "gripper": (-10, 100.0),
}

SO101_FOLLOWER_REST_POSE_RANGE = {
    "shoulder_pan": (0-20.0, 0+20.0), # 0 degree
    "shoulder_lift": (-100.0-20.0, -100.0+20.0), # -100 degree
    "elbow_flex": (90.0-20.0, 90.0+20.0), # 90 degree
    "wrist_flex": (50.0-20.0, 50.0+20.0), # 50 degree
    "wrist_roll": (0.0-20.0, 0.0+20.0), # 0 degree
    "gripper": (-10.0-20.0, -10.0+20.0), # -10 degree
}
