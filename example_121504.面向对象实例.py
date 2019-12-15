#coding=utf-8
#游戏中的角色(战士、法师)
#游戏中的方法(Q\W\E)

class Hero:
    def __init__(self,hero_type,name,blood,q,w,e):
        self.herotype=hero_type   #类型
        self.name=name            #名字
        self.blood=blood          #血量
        self.q=q                  #q技能
        self.e=e                  #e技能
        self.w=w                  #w技能
    def Q(self,enemy):
        print('%s对%s释放Q技能，造成%s伤害，对方血量剩余%s'
              %(self.name,enemy.name,self.q,enemy.blood-self.q))
        #地方血量减少
        enemy.blood-=self.q
        if enemy.blood<=0:
            print('hero %s GG'% enemy.name)
    def W(self,enemy):
        print('%s对%s释放W技能，造成%s伤害，对方血量剩余%s'
              %(self.name,enemy.name,self.w,enemy.blood-self.w))
        #地方血量减少
        enemy.blood-=self.w
        if enemy.blood<=0:
            print('hero %s GG'% enemy.name)
    def E(self,enemy):
        print('%s对%s释放Q技能，造成%s伤害，对方血量剩余%s'
              %(self.name,enemy.name,self.e,enemy.blood-self.e))
        #地方血量减少
        enemy.blood-=self.e
        if enemy.blood<=0:
            print('hero %s GG'% enemy.name)
#选择您的使用英雄
yase=Hero('战士','亚瑟',200,50,30,100)
daji=Hero('法师','妲己',150,10,30,180)

#妲己草丛发现边路亚瑟
daji.E(yase)
yase.W(daji)
yase.E(daji)
yase.Q(daji)
