# coding=utf-8
# Copyright 2019 Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.






from . import *


def build_scenario(builder):
  builder.SetFlag('game_duration', 400)
  builder.SetFlag('deterministic', False)
  builder.SetFlag('offsides', False)
  builder.SetFlag('end_episode_on_score', True)
  builder.SetFlag('end_episode_on_out_of_play', True)
  builder.SetFlag('end_episode_on_possession_change', True)
  builder.SetBallPosition(0.62, 0.0)

  builder.SetTeam(Team.e_Home)
  builder.AddPlayer(-1.0, 0.0, e_PlayerRole_GK)
  builder.AddPlayer(0.6, 0.0, e_PlayerRole_CM)
  builder.AddPlayer(0.7, 0.2, e_PlayerRole_CM)
  builder.AddPlayer(0.7, -0.2, e_PlayerRole_CM)

  builder.SetTeam(Team.e_Away)
  builder.AddPlayer(-1.0, 0.0, e_PlayerRole_GK)
  builder.AddPlayer(-0.75, 0.0, e_PlayerRole_CB)
