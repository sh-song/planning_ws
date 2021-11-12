


def make_global_map(self):
    with open("./map/kcity_map/" + self.map + ".csv", mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)


        for line in csv_reader:
            self.global_path.x.append(float(line[0]))
            self.global_path.y.append(float(line[1]))

            deg_yaw=(degrees(float(line[2]))+360) % 360
            self.global_path.heading.append(deg_yaw)

            self.global_path.k.append(float(line[3]))
            # self.global_path.s.append(float(line[4]))
            self.global_path.env.append(line[5])
            self.global_path.mission.append(line[6])