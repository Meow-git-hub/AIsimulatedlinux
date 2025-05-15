"""
Main entry point for the AI-based simulated OS.
"""

from core_os import SimulatedOS

def main():
    os_env = SimulatedOS()
    os_env.run()

if __name__ == "__main__":
    main()
