
}��]�  �               @   s�   d  Z  d d d g Z d d l Z d d l m Z y d d l m Z Wn" e k
 ri d d l m Z Yn Xd d	 d � Z	 Gd
 d �  d � Z
 d d �  Z e
 �  Z e j Z d S)zGRedo the builtin repr() (representation) but with limits on most sizes.�Repr�repr�recursive_repr�    N)�islice)�	get_identz...c                s   �  f d d �  } | S)zGDecorator to make a repr function return fillvalue for a recursive callc                s�   t  �  �  � �  � f d d �  } t � d � | _ t � d � | _ t � d � | _ t � d � | _ t � d i  � | _ | S)Nc                sW   t  |  � t �  f } | � k r% �  S� j | � z � |  � } Wd  � j | � X| S)N)�idr   �add�discard)�self�key�result)�	fillvalue�repr_running�user_function� �B/media/noha/New Volume/SUShop/backend/env/lib/python3.5/reprlib.py�wrapper   s    z<recursive_repr.<locals>.decorating_function.<locals>.wrapper�
__module__�__doc__�__name__�__qualname__�__annotations__)�set�getattrr   r   r   r   r   )r   r   )r   )r   r   r   �decorating_function   s    	z+recursive_repr.<locals>.decorating_functionr   )r   r   r   )r   r   r      s    c               @   s�   e  Z d  Z d d �  Z d d �  Z d d �  Z d d d	 � Z d
 d �  Z d d �  Z d d �  Z	 d d �  Z
 d d �  Z d d �  Z d d �  Z d d �  Z d d �  Z d d �  Z d S)r   c             C   sg   d |  _  d |  _ d |  _ d |  _ d |  _ 