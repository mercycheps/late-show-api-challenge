from .auth_controller import auth_bp
from .episode_controller import episode_bp
from .guest_controller import guest_bp
from .appearance_controller import appearance_bp

__all__ = ["auth_bp", "episode_bp", "guest_bp", "appearance_bp"]


blueprints = [auth_bp, episode_bp, guest_bp, appearance_bp]