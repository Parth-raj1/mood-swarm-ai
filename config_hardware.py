import psutil

class HardwareConfig:
    def __init__(self):
        self.total_ram_gb = self.get_total_ram()
        self.agent_complexity = self.set_agent_complexity()

    def get_total_ram(self):
        """Return total system RAM in GB."""
        ram_bytes = psutil.virtual_memory().total
        ram_gb = ram_bytes / (1024 ** 3)
        return ram_gb

    def set_agent_complexity(self):
        """
        Determine agent complexity level based on available RAM.
        Example levels: 'low', 'medium', 'high'
        """
        if self.total_ram_gb < 2:
            return 'low'       # Minimal features, fewer parameters
        elif 2 <= self.total_ram_gb < 4:
            return 'medium'    # Moderate features and parameters
        else:
            return 'high'      # Full complexity agents

    def __repr__(self):
        return f"<HardwareConfig total_ram={self.total_ram_gb:.2f}GB, complexity={self.agent_complexity}>"

# Usage example
if __name__ == "__main__":
    config = HardwareConfig()
    print(config)
