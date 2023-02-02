class Valve():
    def __init__(self, name, flow_rate:int, connections):
        self.name = name
        self.flow_rate = flow_rate
        self.connections = connections

    def __repr__(self) -> str:
        return f"Valve('{self.name}', {self.flow_rate}, {self.connections})"

    def __eq__(self, __o: object) -> bool:
        return (self.name == __o.name 
                and self.flow_rate == __o.flow_rate 
                and self.connections == __o.connections)