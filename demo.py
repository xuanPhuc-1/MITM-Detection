class ARPreply:
    def __ini__(self, src_ip, dst_ip, src_mac, dst_mac, packets, timestart):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_mac = src_mac
        self.dst_mac = dst_mac
        
        self.reply_packet = packets
        self.delta_reply_packet = 0.00
        self.timestart =  timestart
        self.avg_reply_pps = 0.00
        self.reply_ins_num = 0.00
        self.reply_last_time = timestart
        
    def update_reply(self, packets, current_time):
        self.delta_reply_packet = packets - self.reply_packet
        self.reply_packet = packets
        
        if self.current_time != self.timestart:
            self.avg_reply_pps = self.delta_reply_packet / float(current_time - self.timestart)
            
        if self.current_time != self.reply_last_time:
            self.reply_ins_num = self.delta_reply_packet / float(current_time - self.reply_last_time)
            
        
        self.reply_last_time = current_time
        
        

