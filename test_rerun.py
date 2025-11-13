import rerun as rr
rr.init("my_robot_viz_application")
rr.connect()  # Connect to a remote viewer
…
rr.log("points", rr.Points3D(positions))
rr.log("camera", rr.Transform3D(pos, rot))
rr.log("camera/image", rr.Pinhole(intrinsics))
rr.log("camera/image", rr.Image(tensor))
rr.log("reprojection_error", rr.Scalar(err))